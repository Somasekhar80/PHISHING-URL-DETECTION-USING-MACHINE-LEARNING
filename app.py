from flask import Flask, render_template, request
import joblib
from feature_extraction import extract_features
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
import os
import re

app = Flask(__name__)

# Load model
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Store last 5 searches
history = []


def is_valid_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        result = urlparse(url)
        return bool(result.netloc and "." in result.netloc)
    except:
        return False


def capture_screenshot(url):
    try:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1366,768")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        if not url.startswith("http"):
            url = "https://" + url

        if not os.path.exists("static"):
            os.makedirs("static")

        filename = "static/preview.png"

        driver.get(url)
        driver.save_screenshot(filename)
        driver.quit()

        return filename

    except Exception as e:
        print("Screenshot Error:", e)
        return None


def analyze_url(url):
    breakdown = {
        "Contains IP Address": bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)),
        "Contains @ Symbol": "@" in url,
        "Too Long URL (>75 chars)": len(url) > 75,
        "Too Many Dots (>3)": url.count(".") > 3
    }

    blacklist = [
        "paypal-login-secure.com",
        "amazon-verify-account.net",
        "google-auth-reset.xyz",
        "freegiftclaim.click",
        "securebankverify.net"
    ]

    blacklisted = any(bad in url for bad in blacklist)

    risk_score = 0
    for value in breakdown.values():
        if value:
            risk_score += 25

    if blacklisted:
        risk_score = 100

    return breakdown, risk_score, blacklisted


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    global history

    url = request.form['url'].strip()

    # URL Validation
    if not is_valid_url(url):
        return render_template(
            "result.html",
            result="❌ Invalid URL. Please enter a real website.",
            url=url,
            legitimate=0,
            phishing=0,
            ip_address="N/A",
            certificate="N/A",
            hosting_provider="N/A",
            location="N/A",
            history=history,
            preview_path=None,
            breakdown={},
            risk_score=0,
            blacklisted=False
        )

    try:
        features, ip_address, certificate, hosting_provider, location = extract_features(url)

        url_vector = vectorizer.transform([url])

        prediction = model.predict(url_vector)[0]
        proba = model.predict_proba(url_vector)[0]

        legitimate = round(float(proba[0]) * 100, 2)
        phishing = round(float(proba[1]) * 100, 2)

        if prediction == 1:
            result = "⚠️ Phishing Website"
        else:
            result = "✅ Legitimate Website"

        preview_path = capture_screenshot(url)
        breakdown, risk_score, blacklisted = analyze_url(url)

        history.append({
            "url": url,
            "result": result,
            "legitimate": legitimate,
            "phishing": phishing
        })

        history = history[-5:]

        return render_template(
            "result.html",
            result=result,
            url=url,
            legitimate=legitimate,
            phishing=phishing,
            ip_address=ip_address,
            certificate=certificate,
            hosting_provider=hosting_provider,
            location=location,
            history=history,
            preview_path=preview_path,
            breakdown=breakdown,
            risk_score=risk_score,
            blacklisted=blacklisted
        )

    except Exception as e:
        return render_template(
            "result.html",
            result=f"Error: {str(e)}",
            url=url,
            legitimate=0,
            phishing=0,
            ip_address="N/A",
            certificate="N/A",
            hosting_provider="N/A",
            location="N/A",
            history=history,
            preview_path=None,
            breakdown={},
            risk_score=0,
            blacklisted=False
        )


if __name__ == "__main__":
    app.run(debug=True)

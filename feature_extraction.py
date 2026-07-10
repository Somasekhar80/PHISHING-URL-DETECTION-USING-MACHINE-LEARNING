import socket, ssl, requests, os
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_features(url):
    features = {}
    parsed = urlparse(url)
    domain = parsed.netloc

    # Dataset features
    features['at_symbol'] = 1 if '@' in url else 0
    features['isHttps'] = 1 if url.lower().startswith("https") else 0
    features['nb_and'] = url.count('&')
    features['nb_com'] = url.count('com')
    features['nb_dots'] = url.count('.')

    # Extra details
    try:
        ip_address = socket.gethostbyname(domain)
    except:
        ip_address = "Unknown"

    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(3)
            s.connect((domain, 443))
            cert = s.getpeercert()
            certificate = cert.get('issuer')[0][0][1]
    except:
        certificate = "Unknown"

    try:
        resp = requests.get(f"https://ipinfo.io/{ip_address}/json", timeout=5)
        data = resp.json()
        hosting_provider = data.get("org", "Unknown")
        location = data.get("country", "Unknown")
    except:
        hosting_provider, location = "Unknown", "Unknown"

    return features, ip_address, certificate, hosting_provider, location

def get_screenshot(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1024, 768)
    driver.get(url)

    screenshot_path = os.path.join("static", "preview.png")
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path

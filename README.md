# PHISHING-URL-DETECTION-USING-MACHINE-LEARNING
Phishing URL Detection Using Machine Learning is a Flask-based web application that detects malicious URLs by extracting URL features and using a trained Machine Learning model to classify websites as phishing or legitimate.
# 🔐 Phishing URL Detection Using Machine Learning

A Flask-based web application that detects whether a website URL is **Legitimate** or **Phishing** using a Machine Learning model. The application provides real-time URL analysis, confidence scores, website preview screenshots, feature breakdown, blacklist checking, and recent search history.

---

## 📌 Features

- 🔍 Detects phishing and legitimate URLs using Machine Learning
- 📊 Displays Legitimate and Phishing confidence percentages
- 📷 Website screenshot preview using Selenium
- ⚠️ URL risk score calculation
- 🚫 Blacklist URL checking
- 📋 URL feature breakdown
- 🕒 Displays the last 5 search results
- 🌐 Simple and responsive Flask web interface
- ✅ URL validation before prediction

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Joblib
- TF-IDF Vectorizer

### Libraries
- Pandas
- NumPy
- Selenium
- WebDriver Manager
- urllib
- Regular Expressions (re)

---

## 📂 Project Structure

```
Phishing-URL-Detection/
│
├── app.py
├── feature_extraction.py
├── train.py
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── preview.png
│
├── dataset/
│   └── phishing_urls.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/phishing-url-detection.git

cd phishing-url-detection
```

---

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📷 Application Workflow

1. Enter a Website URL.
2. Click **Scan Website**.
3. URL is validated.
4. Features are extracted.
5. TF-IDF converts the URL into vectors.
6. Machine Learning predicts the result.
7. Website screenshot is captured.
8. Risk score is calculated.
9. Blacklist is checked.
10. Results are displayed.

---

## 📊 Output

The application displays

- Prediction Result
- Legitimate Percentage
- Phishing Percentage
- Website Screenshot
- URL Feature Breakdown
- Risk Score
- IP Address
- SSL Certificate
- Hosting Provider
- Location
- Blacklist Status
- Search History

---

## 📁 Machine Learning Model

The model is trained using phishing and legitimate URL datasets.

Algorithm Used

- Random Forest Classifier

Vectorization

- TF-IDF Vectorizer

Model files

```
model/model.pkl
model/vectorizer.pkl
```

---

## 📸 Screenshots

### Home Page

Add your screenshot here.

---

### Prediction Result

Add your screenshot here.

---

### Website Preview

Add your screenshot here.

---

## 🚀 Future Enhancements

- Browser Extension
- Mobile Application
- Live Threat Intelligence
- Deep Learning Models
- User Login System
- Cloud Deployment
- Automatic Model Updates
- API Integration

---

## 📚 Project Objective

The objective of this project is to develop a Machine Learning-based web application capable of detecting phishing websites by analyzing URL characteristics. The system helps users identify malicious websites before accessing them, thereby improving cybersecurity and reducing phishing attacks.

---

## 👨‍💻 Author

**Soma Sekhar**

MCA Graduate

---

## 📄 License

This project is developed for educational and research purposes.

---

⭐ If you found this project useful, don't forget to **Star** this repository.

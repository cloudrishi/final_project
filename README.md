# 🎭 AI-Based Emotion Detection

A Flask-based web application that detects emotions from text using IBM Watson NLP EmotionPredict service. Built as the final project for the IBM AI Developer Professional Certificate.

---

## 🚀 What It Does

Analyzes text and returns emotion scores across 5 dimensions with a dominant emotion:

```json
{
  "anger": 0.0023,
  "disgust": 0.0012,
  "fear": 0.0034,
  "joy": 0.9687,
  "sadness": 0.0021,
  "dominant_emotion": "joy"
}
```

---

## 🏗️ Architecture

```
Browser
   │
   ▼
Flask REST API (server.py)
   │
   ▼
EmotionDetection Module
   │
   ▼
IBM Watson NLP EmotionPredict Service
   │
   ▼
emotion_aggregated-workflow_lang_en_stock model
```

---

## 🛠️ Tech Stack

- **Python 3.11** — core language
- **Flask** — REST API and web server
- **IBM Watson NLP** — emotion detection model
- **Requests** — HTTP client

---

## 🎯 Detected Emotions

| Emotion    | Description             |
| ---------- | ----------------------- |
| 😠 Anger   | Detects anger in text   |
| 🤢 Disgust | Detects disgust in text |
| 😨 Fear    | Detects fear in text    |
| 😊 Joy     | Detects joy in text     |
| 😢 Sadness | Detects sadness in text |

---

## ⚙️ Installation

```bash
# Clone the repo
git clone git@github.com:cloudrishi/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> **Note:** This application requires access to IBM Watson NLP services via IBM Skills Network.

---

## 🎯 Usage

**Start the server:**

```bash
python server.py
```

**Analyze emotions via curl:**

```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I am so happy today!"
```

**Or open the web UI:**

```
http://localhost:5000
```

---

## 🧪 Run Tests

```bash
python -m unittest test_emotion_detection.py -v
```

Sample output:

```
Statement                                     Dominant Emotion
--------------------------------------------------------------
I am glad this happened                       joy
I am really mad about this                    anger
I feel disgusted just hearing about this      disgust
I am so sad about this                        sadness
I am really afraid that this will happen      fear
```

---

## 📁 Project Structure

```
oaqjp-final-project-emb-ai/
  ├── server.py                    # Flask REST API
  ├── test_emotion_detection.py    # Unit tests
  ├── EmotionDetection/            # Core emotion detection module
  │   └── emotion_detection.py
  ├── static/                      # CSS and JS
  ├── templates/                   # HTML templates
  └── README.md
```

---

## 🏆 Certificate

Built as the final project for the **IBM AI Developer Professional Certificate** on Coursera.

---

## 👨‍💻 Author

**Rishi Pherwani**
Senior Technical Architect | Full Stack Engineer | AI/ML Enthusiast
[LinkedIn](https://linkedin.com/in/rishipherwani) • [GitHub](https://github.com/cloudrishi)

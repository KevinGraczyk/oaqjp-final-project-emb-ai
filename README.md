# Emotion Detection System (Watson NLP)

Professional AI-driven web application designed to analyze text and detect underlying emotions. This project was developed as part of the **AI Developer Professional Certificate**.

## 🚀 Project Overview
The application takes user-provided text through a web interface and processes it using the **IBM Watson NLP library**. It identifies five key emotions: **anger, disgust, fear, joy, and sadness**, and determines the **dominant emotion**.

### Key Features
- **Custom Python Package:** Modular code structure with a dedicated `EmotionDetection` package.
- **RESTful API:** Flask-based server providing an endpoint for emotion analysis.
- **Robust Error Handling:** Specifically handles empty inputs (400 Bad Request) by returning null-safe responses.
- **Unit Testing:** Comprehensive test suite using Python's `unittest` framework to ensure logic accuracy.
- **Static Code Analysis:** Achieved a perfect **10/10 Pylint score**, adhering to PEP 8 standards.

## 🛠️ Technology Stack
- **Language:** Python 3
- **Framework:** Flask
- **AI/ML API:** IBM Watson NLP
- **Testing:** Unittest
- **Linting:** Pylint

## 📁 Project Structure
```text
.
├── EmotionDetection/        # Custom package for logic
│   ├── __init__.py          # Package initialization
│   └── emotion_detection.py # Watson API integration
├── static/                  # Web assets (JS & CSS)
├── templates/               # HTML templates (Flask)
├── server.py                # Main Flask application
├── test_emotion_detection.py# Unit tests
└── README.md                # Project documentation


# Scam Message Investigator

## Overview
Scam Message Investigator is a Python-based application developed using Streamlit. It helps users identify suspicious messages in Tamil and English.

The application analyzes SMS messages, emails, job offers, and online messages using keyword-based detection techniques.

## Features
- Tamil and English message screening
- SMS, Email, Job Offer, and Online Message analysis
- Suspicious link detection
- OTP and password request detection
- Fake job offer indicators
- Lottery and prize scam detection
- Payment request detection
- Instant investigation results
- Safety recommendations

## Technologies Used
- Python
- Streamlit
- Regular Expressions (Regex)

## Project Structure

```text
Scam-Message-Investigator/
│
├── scam.py
├── reqy.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Scam-Message-Investigator
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Install Dependencies

```bash
pip install -r reqy.txt
```

### 5. Run the Application

```bash
python -m streamlit run scam.py
```

## How It Works

1. Select the message type.
2. Enter a Tamil or English message.
3. Click the Investigate Message button.
4. The application checks for suspicious keywords and patterns.
5. View the investigation report and safety recommendations.

## DEMO
## Screenshot
<img width="1920" height="1080" alt="Screenshot (193)" src="https://github.com/user-attachments/assets/40afebf2-b6a3-4ed8-83a2-c7e3512325b0" />

<img width="1920" height="1080" alt="Screenshot (194)" src="https://github.com/user-attachments/assets/32fca5e0-dd72-4b40-99ef-bf52405deec3" />

<img width="1920" height="1080" alt="Screenshot (195)" src="https://github.com/user-attachments/assets/90de9bb8-cadf-4019-a7a8-393faf1d3bd0" />

<img width="1920" height="1080" alt="Screenshot (197)" src="https://github.com/user-attachments/assets/0dffe284-83c5-4ae3-a036-9ef8e2ea5df1" />

<img width="1920" height="1080" alt="Screenshot (198)" src="https://github.com/user-attachments/assets/2c66c4f2-3e50-4935-9393-a8a41f6bb399" />


## Limitations

- Uses rule-based keyword detection.
- May not identify every type of scam.
- Messages without known suspicious patterns may still be fraudulent.
- Results should not be treated as a guarantee of message authenticity.

## Future Enhancements
- Integration with multilingual AI models.
- Improved scam detection accuracy.
- URL safety checking.
- Advanced phishing detection.

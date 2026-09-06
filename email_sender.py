# Python Keylogger (For Educational Use Only)

This is a **Python-based keylogger** that records all keystrokes on a machine and logs them to a file. Optionally, it can send the log file to your email for remote monitoring and auditing purposes.

 **Disclaimer**: This project is created strictly for **educational**, **ethical hacking**, or **self-auditing** purposes. Using it on anyone's device without **explicit consent** is illegal and unethical.


## Features

-  Logs all keystrokes in the background
-  Saves keystrokes to `keylog.txt`
-  Sends log file via email (Gmail SMTP)
-  Optional stealth mode (hide terminal)
-  Lightweight and simple


##  Setup Instructions

### 1. Clone the Repository

bash-
git clone https://github.com/itzRajdeep143/KEYLOGGER_PROJECT
cd Keylogger-Project

### 2. Install Dependencies
bash-
pip install pynput

bash-
pip install pillow

### Run the Keylogger
bash-
python keylogger.py

### Folder Structure

python-keylogger
├── keylogger.py
├── email_sender.py
├── keylog.txt
├── README.md
└── requirements.txt (optional)


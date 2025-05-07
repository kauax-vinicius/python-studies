# 📧 Email Reader Automation / Automação de Leitura de E-mails

This Python project connects to your Gmail inbox, reads today's emails, and generates a simple report showing the sender, subject, and date.

---

## 🇬🇧 English

### Features

✅ Connects to Gmail using IMAP  
✅ Searches for emails from today  
✅ Decodes the subject correctly  
✅ Generates a text report  
✅ Prints the report in the console

### Requirements

- Python 3.x
- Libraries:
  - imaplib
  - email
  - datetime

### Setup

1. Enable 2-Step Verification on your Google account.
2. Generate an **App Password** in Google Security settings.
3. Replace the `user` and `password` variables in `main.py`:
   ```python
   user = 'your_email@gmail.com'
   password = 'your_app_password'

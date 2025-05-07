import imaplib
import email
from email.header import decode_header
import datetime

# your email
user = ''
# your password
password = ''
imap_server = 'imap.gmail.com'

try:
    server = imaplib.IMAP4_SSL(imap_server)
    server.login(user, password)
    server.select('INBOX')

    date = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d-%b-%Y')  # Corrigi formato de data para 'SINCE'
    status, messages = server.search(None, f'(SINCE {date})')
    emails_ids = messages[0].split()
    report = []

    for num in emails_ids:
        status, data = server.fetch(num, '(RFC822)')
        message = email.message_from_bytes(data[0][1])
        sender = message['From']
        subject, encoding = decode_header(message['Subject'])[0]

        if isinstance(subject, bytes):
            subject = subject.decode(encoding or 'utf-8')

        date_msg = message['Date']
        report.append(f'From: {sender}\nSubject: {subject}\nDate: {date_msg}\n')

    for item in report:
        print(item)
        print('-' * 50)

    server.logout()

except Exception as error:
    print(error)

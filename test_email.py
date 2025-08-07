import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_test_email():
    sender_email = 'nammajalofficial@gmail.com'
    receiver_email = 'poojamurugesan2702@gmail.com'
    password = 'mtok nyjl dzvs chhx'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Test Email'
    
    body = 'This is a test email.'
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Test email sent successfully")
    except Exception as e:
        print(f"Failed to send test email: {e}")

send_test_email()

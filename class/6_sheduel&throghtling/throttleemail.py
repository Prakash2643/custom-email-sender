import time
import sendemail

def throttle_email_sending(email_list, subject, body, delay):
    for email in email_list:
        sendemail(subject, body, email)
        time.sleep(delay)
        
email_list = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]
subject = "Your Throttled Email"
body = "This is a test email sent with throttling."
delay = 10  # Delay in seconds

throttle_email_sending(email_list, subject, body, delay)

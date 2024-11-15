import schedule
import time
import sendemail

def schedule_email(subject, body, to_email, send_time):
    schedule.every().day.at(send_time).do(sendemail, subject, body, to_email)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
subject = "Your Scheduled Email"
body = "This is a test email sent at a scheduled time."
to_email = "recipient@example.com"
send_time = "10:30"  # Time in HH:MM format

schedule_email(subject, body, to_email, send_time)

import sendgrid
from sendgrid.helpers.mail import Mail

def send_email(subject, body, to_email):
    sg = sendgrid.SendGridAPIClient(api_key='your_sendgrid_api_key')
    from_email = 'your_email@example.com'
    to_email = to_email
    content = body
    mail = Mail(from_email, to_email, subject, content)
    response = sg.send(mail)
    print(response.status_code)
    print(response.body)
    print(response.headers)

send_email("Test Subject", "This is a test email body", "recipient@example.com")

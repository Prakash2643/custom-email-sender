def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

for index, row in df.iterrows():
    company_name = row['Company Name']
    location = row['Location']
    email = row['Email']
    products = row['Products']
    prompt = "Write a professional email to {company_name} located in {location} about their products: {products}."
    email_content = generate_email_content(prompt, company_name, location, products)
    send_email("Subject: Your Products", email_content, email)

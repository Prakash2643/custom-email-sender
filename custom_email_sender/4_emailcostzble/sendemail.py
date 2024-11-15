import pythonscript
for index, row in df.iterrows():
    company_name = row['Company Name']
    location = row['Location']
    products = row['Products']
    prompt = "Write a professional email to {company_name} located in {location} about their products: {products}."
    email_content = generate_email_content(prompt, company_name, location, products)
    print(f"Email to {company_name}:\n{email_content}\n")

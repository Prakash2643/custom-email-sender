for index, row in df.iterrows():
    company_name = row['Company Name']
    location = row['Location']
    email = row['Email']
    products = row['Products']
    print(f"Company: {company_name}, Location: {location}, Email: {email}, Products: {products}")

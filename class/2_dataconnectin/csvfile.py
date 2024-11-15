import pandas as happy

# Read the CSV file
df = happy.read_csv('A:\class\Book1.csv')

# Display the data
print(df.head())

for index, row in df.iterrows():
    company_name = row['Company Name']
    location = row['Location']
    email = row['Email']
    products = row['Products']
    print(f"Company: {company_name}, Location: {location}, Email: {email}, Products: {products}")


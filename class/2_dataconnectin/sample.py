from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials from the JSON file
creds = service_account.Credentials.from_service_account_file('A:\class\credentials.json')

# Build the service
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId='384545620724-urc902jdm0evhd71ik1s5s5g6i5knlkm.apps.googleusercontent.com', range='Sheet1!A1:D10').execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    for row in values:
        print(row)

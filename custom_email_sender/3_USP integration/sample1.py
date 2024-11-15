from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials from the JSON file
creds = service_account.Credentials.from_service_account_file('A:\class\credentials1.json')

# Build the service
service = build('gmail', 'v1', credentials=creds)

# Call the Gmail API
results = service.users().messages().list(userId='me').execute()
messages = results.get('messages', [])

if not messages:
    print('No messages found.')
else:
    for message in messages:
        print(message)

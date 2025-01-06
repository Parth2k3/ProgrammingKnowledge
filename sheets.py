import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'gcp_key.json'

credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Sheets API client
service = build('sheets', 'v4', credentials=credentials)

spreadsheet_id = '1-DTUXcYKvl07WjAyQyEP3tLMQeDdZysZDhiEBCH2PSA'
range_name = 'Sheet1!A1:A5'  # Example range

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

values = result.get('values', [])
if not values:
    print('No data found.')
else:
    for row in values:
        print(row)



values = [
    ['Name', 'Age'],
    ['Alice', 25],
    ['Bob', 30]
]
body = {'values': values}

result = sheet.values().update(
    spreadsheetId=spreadsheet_id, range='Sheet1!A1:B3',
    valueInputOption='RAW', body=body).execute()

print(f"{result.get('updatedCells')} cells updated.")

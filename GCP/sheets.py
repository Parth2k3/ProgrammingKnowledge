

import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
#STANDARD GOOGLE SHEETS API SETUP
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SERVICE_ACCOUNT_FILE = "gcp_key.json"

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()

sheet_id = '1-DTUXcYKvl07WjAyQyEP3tLMQeDdZysZDhiEBCH2PSA'

range = 'A1:A5'
###
#READ SHEET FUNCTION
sheet_read = sheet.values().get(spreadsheetId=sheet_id, range=range).execute()

values = sheet_read.get('values', [])
for row in values:
    print(row)
###


#WRITE/UPDATE SHEET FUNCTION
values = [
    ['Hello', 'World'],
    ['Hello2', 'World2']
]
body = {'values': values}

sheet_write = sheet.values().update(spreadsheetId=sheet_id, range='A1:B2', valueInputOption='RAW', body=body).execute()
sheet_read = sheet.values().get(spreadsheetId=sheet_id, range=range).execute()
values = sheet_read.get('values', [])
for row in values:
    print(row)
###

#CLEAR SHEET FUNCTION
sheet_clear = sheet.values().clear(spreadsheetId=sheet_id, range='A1:B2').execute()
sheet_read = sheet.values().get(spreadsheetId=sheet_id, range=range).execute()
values = sheet_read.get('values', [])
for row in values:
    print(row)
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Authenticate with the Google Drive API
credentials = service_account.Credentials.from_service_account_file('client_auth.json')
drive_service = build('drive', 'v3', credentials=credentials)

# Specify the folder ID
folder_id = '1dLzxWmF9c0ZDiAUQG9-9uAsXkUm6751O'

# List all files in the specified folder
results = drive_service.files().list(q=f"'{folder_id}' in parents and trashed=false", fields="files(id, name)").execute()
files = results.get('files', [])

from googleapiclient.discovery import build

# Replace with your folder ID
folder_id = "1dLzxWmF9c0ZDiAUQG9-9uAsXkUm6751O"

# Authenticate with Google Drive API (refer to official documentation for details)
# https://developers.google.com/drive/api/v3/quickstart/python
drive_service = build('drive', 'v3')

# Define the search query
query = f"mimeType='application/vnd.google-apps.spreadsheet' and parents in '{folder_id}'"

# Retrieve files based on the query
response = drive_service.files().list(q=query, fields="nextPageToken, files(id)").execute()

# Extract spreadsheet IDs from the response
spreadsheet_ids = [file['id'] for file in response.get('files', [])]

# Print the retrieved spreadsheet IDs
print(spreadsheet_ids)

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import gspread

import pandas as pd


flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    "client_secrets.json",
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)
flow.run_local_server(authorization_prompt_message='')
credentials = flow.credentials


client = gspread.authorize(credentials)


if __name__ == '__main__':
    # Create a new Google Sheet
    spreadsheet = client.create('My New Spreadsheet')

    # Select the first sheet
    sheet = spreadsheet.get_worksheet(0)

    # Example DataFrame
    df = pd.DataFrame({
        'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']
    })

    # Upload DataFrame to the Google Sheet
    sheet.update([df.columns.tolist()] + df.values.tolist())

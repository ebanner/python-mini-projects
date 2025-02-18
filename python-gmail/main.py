from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
creds = flow.run_local_server(port=0)

service = build("gmail", "v1", credentials=creds)


if __name__ == '__main__':
    results = service.users().messages().list(userId="me", maxResults=5).execute()
    messages = results.get("messages", [])
    msg = messages[0]

    msg_id = msg["id"]
    msg_data = service.users().messages().get(userId="me", id=msg_id, format="full").execute()

    print(msg_data)


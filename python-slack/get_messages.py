from slack_sdk import WebClient

SLACK_BOT_TOKEN = ...

client = WebClient(token=SLACK_BOT_TOKEN)

response = client.conversations_history(
    channel="C04C5AVUMQF",
    limit=10
)

response.data

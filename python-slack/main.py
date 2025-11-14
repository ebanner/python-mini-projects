from slack_sdk import WebClient

SLACK_BOT_TOKEN = ...

slack_client = WebClient(SLACK_BOT_TOKEN)

response = slack_client.chat_postMessage(
    channel='general',
    text='Hello!'
)

response.data

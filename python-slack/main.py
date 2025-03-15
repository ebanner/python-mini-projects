import os

from dotenv import load_dotenv
load_dotenv()

from slack_sdk import WebClient

SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']

slack_client = WebClient(SLACK_BOT_TOKEN)


if __name__ == '__main__':
    response = slack_client.chat_postMessage(
        channel='general',
        text='Hello!'
    )

    print(response.data)

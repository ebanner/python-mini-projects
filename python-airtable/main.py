import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

BEARER_TOKEN = os.environ['BEARER_TOKEN']


def get_records():
    response = requests.get(
        "https://api.airtable.com/v0/app29Tvdy4klt3OH1/Table%201",
        headers={
        "Authorization": f"Bearer {BEARER_TOKEN}"
    })
    records = response.json()
    return records


if __name__ == '__main__':
    records = get_records()
    print(records)

    #
    # Update a record
    #
    response = requests.patch(
        'https://api.airtable.com/v0/app29Tvdy4klt3OH1/Table%201',
        data=json.dumps({
            'records': [
                {
                    "id": "recRuP6atScHyqB3Z",
                    "fields": {
                        "Name": "Eddie"
                    }
                }
            ]
        }),
        headers={
            "Authorization": f"Bearer {BEARER_TOKEN}",
            "Content-Type": "application/json"
        }
    )

    records = get_records()
    print(records)


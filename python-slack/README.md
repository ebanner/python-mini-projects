# python-slack

Send a message with the slack SDK

## usage

```
% python main.py
{
  "ok": true,
  "channel": "C04C5AVUMQF",
  "ts": "1736608909.051679",
  "message": {
    "user": "U04D9N8FPLY",
    "type": "message",
    "ts": "1736608909.051679",
    "bot_id": "B04CH36DN13",
    "app_id": "A04CKTX53EF",
    "text": "Hello!",
    "team": "T04CKSUTLDQ",
    "bot_profile": {
      "id": "B04CH36DN13",
      "app_id": "A04CKTX53EF",
      "name": "Awakened Bot",
      "icons": {
        "image_36": "https://avatars.slack-edge.com/2025-01-05/8262463810737_27e418c48bac64257091_36.png",
        "image_48": "https://avatars.slack-edge.com/2025-01-05/8262463810737_27e418c48bac64257091_48.png",
        "image_72": "https://avatars.slack-edge.com/2025-01-05/8262463810737_27e418c48bac64257091_72.png"
      },
      "deleted": false,
      "updated": 1736109647,
      "team_id": "T04CKSUTLDQ"
    },
    "blocks": [
      {
        "type": "rich_text",
        "block_id": "mFrh5",
        "elements": [
          {
            "type": "rich_text_section",
            "elements": [
              {
                "type": "text",
                "text": "Hello!"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

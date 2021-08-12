from slackbot-modules import google-calendar
from slackbot-modules import weather
#slackbot関連
import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token = slack_token)

def morning():
    slack_message
     try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text=slack_message 
        )
    except SlackApiError as e:
        assert e.response["error"]
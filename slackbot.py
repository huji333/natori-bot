from SlackbotModules import GoogleCalendar
from SlackbotModules import Weather
#slackbot関連
import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token = slack_token)

#おはように対して
def morning():
    slack_message = "おはようございナース:eggplant:"+"\n"+GoogleCalendar.GetEvents()
    try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text=slack_message 
        )
    except SlackApiError as e:
        assert e.response["error"]
morning()
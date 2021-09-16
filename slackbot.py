from SlackbotModules import GoogleCalendar
from SlackbotModules import Weather
import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token = slack_token)

def morning():
    slack_message = "おはようございナース:eggplant:\n\n"+Weather.GetWeather()+GoogleCalendar.GetEvents()+"*課題*\nなし!"
    try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text=slack_message 
        )
    except SlackApiError as e:
        assert e.response["error"]

if __name__=="__main__":
    morning()
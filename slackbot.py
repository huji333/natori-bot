from SlackbotModules import GoogleCalendar
from SlackbotModules import Weather
from SlackbotModules import Assignments
import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token = slack_token)

def morning():
    slack_message = "おはようございナース:eggplant:\n"+Weather.get_weather()+GoogleCalendar.get_events()+Assignment.get_assignments()
    try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text=slack_message 
        )
    except SlackApiError as e:
        assert e.response["error"]

def slept():
    try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text="ふじくんが寝ました!"
        )
    except SlackApiError as e:
        assert e.response["error"]


def returned():
    try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text="ふじくんが帰ってきました!"
        )
    except SlackApiError as e:
        assert e.response["error"]
        
def gone():
    try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text="ふじくんが出かけました!"
        )
    except SlackApiError as e:
        assert e.response["error"]

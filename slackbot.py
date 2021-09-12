from SlackbotModules import GoogleCalendar
from SlackbotModules import Weather
#slackbot
import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token = slack_token)

#In responce to "Good Morning"
def morning():
    #get weather
    # url = "https://www.jma.go.jp/bosai/forecast/data/forecast/260000.json"
    # filename = "weather.json"
    # urllib.request.urlretrieve(url,filename)

    slack_message = "おはようございナース:eggplant:\n\n"+Weather.GetWeather()#+GoogleCalendar.GetEvents()
    try:
        response = client.chat_postMessage(
            channel="C02A7S2JGU9",
            text=slack_message 
        )
    except SlackApiError as e:
        assert e.response["error"]
morning()
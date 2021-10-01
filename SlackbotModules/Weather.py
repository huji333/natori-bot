import json
import urllib.request
def get_weather():
    #Retrieve .json
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/260000.json"
    filename = "weather.json"
    urllib.request.urlretrieve(url,filename)
    with open("weather.json","r",encoding="UTF-8") as f:
        weather_data=json.load(f)

    #Slack message
    message = "\n*天気*\n"+weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][0]+"\n>*降水確率*　"
    for i in range(4):
        message+=(weather_data[0]["timeSeries"][1]["timeDefines"][i][11:16]+"-:"+weather_data[0]["timeSeries"][1]["areas"][0]["pops"][i]+"%　")
    message+=("\n>*気温*　"+weather_data[0]["timeSeries"][2]["areas"][0]["temps"][1]+"　"+weather_data[0]["timeSeries"][2]["areas"][0]["temps"][2])
    message+=("\n>*明日の天気*　"+weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][1]+"\n")
    return message


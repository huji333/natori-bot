import json
import urllib.request
def GetWeather():
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/260000.json"
    filename = "weather.json"
    urllib.request.urlretrieve(url,filename)
    with open("weather.json","r",encoding="UTF-8") as f:
        WeatherData=json.load(f)
    message = "*天気*\n"+WeatherData[0]["timeSeries"][0]["areas"][0]["weathers"][0]+"\n>*降水確率*　"
    for i in range(4):
        message+=(WeatherData[0]["timeSeries"][1]["timeDefines"][i][11:16]+"-:"+WeatherData[0]["timeSeries"][1]["areas"][0]["pops"][i]+"%　")
    message+=("\n>*気温*　"+WeatherData[0]["timeSeries"][2]["areas"][0]["temps"][0]+"　"+WeatherData[0]["timeSeries"][2]["areas"][0]["temps"][1])
    message+=("\n\n明日の天気は、"+WeatherData[0]["timeSeries"][0]["areas"][0]["weathers"][1]+"　なのです。\n")
    return message
#     print(message)
# GetWeather()


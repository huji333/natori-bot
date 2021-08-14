import json
def GetWeather():
    
    with open("weather.json","r",encoding="UTF-8") as f:
        WeatherData=json.load(f)
    message = "今日の天気は、"+WeatherData[0]["timeSeries"][0]["areas"][0]["weathers"][0]+"　なのです。\n降水確率　"
    for i in range(4):
        message+=(WeatherData[0]["timeSeries"][1]["timeDefines"][i][11:16]+"-:"+WeatherData[0]["timeSeries"][1]["areas"][0]["pops"][i]+"%　")
    message+=("\n気温:　"+WeatherData[0]["timeSeries"][2]["areas"][0]["temps"][0]+"　"+WeatherData[0]["timeSeries"][2]["areas"][0]["temps"][1])
    message+=("\n\n明日の天気は、"+WeatherData[0]["timeSeries"][0]["areas"][0]["weathers"][1]+"　なのです。\n")
    return message
#GetWeather()
    


import os 
import json
import datetime
from slack_bolt import App
from datetime import datetime
from datetime import timedelta
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(
    token = os.environ.get("SLACK_BOT_TOKEN"),
)
@app.command("/set-huji333's-alarm")
def repeat_text(ack, respond,command):
    ack()
    #encode in Alarm.json
    snoozeDatetime=datetime.strptime(command['text'],"%H:%M")+timedelta(minutes=5)
    jsonObject = {
        "alarm":command['text'],
        "snooze":snoozeDatetime.strftime("%H:%M")
    }
    file = open("Alarm.json","w")
    json.dump(jsonObject,file)
    file.close()

    respond(command['text']+"にアラームをセットしました!")

if __name__ == "__main__":
    SocketModeHandler(app,os.environ["SLACK_APP_TOKEN"]).start()

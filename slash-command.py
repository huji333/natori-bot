import os 
import speaker
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(
    token = os.environ.get("SLACK_BOT_TOKEN"),
)
@app.command("/set-huji333's-alarm")
def repeat_text(ack, respond,command):
    ack()
    print(command['text'])
    speaker.set_alarm(command['text'])
    respond(command['text']+"にアラームをセットしました!")

if __name__ == "__main__":
    SocketModeHandler(app,os.environ["SLACK_APP_TOKEN"]).start()

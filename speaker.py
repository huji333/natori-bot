import datetime
import slackbot


alarm="10:00"
def set_alarm(t):
    alarm=t

# word="OHAYOU"
# awake = False
# if word=="OHAYOU":
#     if not awake:
#         slackbot.morning()
#         playsound
#         awake = True
# if word=="OYASUMI":
#     awake = False
# if word=="ITTEKIMASU"
#     playsound
# if word=="TADAIMA"
#     playsound

now = datetime.datetime.now().strftime("%H:%M")
# if now == alarm:
#     playsound()
# if now == "22:00":
#     playsound()
# if now == "23:00":
#     playsound()
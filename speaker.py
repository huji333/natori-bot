import socket
import time
import datetime
import json
import slackbot
from pygame import mixer
from datetime import timedelta
from datetime import datetime

def play_audio(path,n):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play(n)

def read_json(s):
    with open("Alarm.json","r") as f:
        alarmData=json.load(f)
    return alarmData[s]

#Alarm and reminders
def ring_alarm(x):
    if x=='a':
        if not awake:
            play_audio("Voices/Okitemasuka.wav",3)
    if x=='s':
        if not awake:
            play_audio("Voices/Okite.wav",5)
def reminder(x):
    if x=="22":
        play_audio("Voices/2200.wav",0)
    if x=="23":
        play_audio("Voices/2300.wav",0)


awake = False
host='localhost'
port=10500
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,port))
res=''

#julius
while True:
    while (res.find('\n.')==-1):
        res+=sock.recv(1024)

    word=""
    for line in res.split('\n'):
        index=line.find('WORD=')
        if index != -1:
            line=line[index+6:line.find('"',index+6)]
        if line != '[s]':
            word+=line

    if word == "おはよう":
        pygame.mixer.music.stop()
        if not awake:
            awake = True
            if datetime.strptime(datetime.now().strftime("%H:%M"),"%H:%M")<datetime.strptime("11:00","%H:%M"):
                play_audio("Voices/Ohayou.wav",0)
            else:
                play_audio("Voices/konnichiwa.wav",0)
            slackbot.morning()
    if word == "おやすみ":
        awake = False
        play_audio("Voices/Oyasumi.wav",0)
    if word == "いってきます":
        play_audio("Voices/Itterassyai.wav",0)
    if word == "ただいま":
        play_audio("Voices/okaeri.wav",0)

#alarm
while True:
    if datetime.now().strftime("%H:%M")==read_json("alarm"):
        ring_alarm("a")
    if datetime.now().strftime("%H:%M")==read_json("snooze"):
        ring_alarm("s")
    if datetime.now().strftime("%H:%M")=="22:00":
        reminder("22")
    if datetime.now().strftime("%H:%M")=="23:00":
        reminder("23")
    time.sleep(60)

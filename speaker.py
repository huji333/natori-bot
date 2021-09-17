import socket
import time
import datetime
import json
import slackbot
import pygame
import audio
from datetime import timedelta
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def play_audio(path,n):
    print("audio")
    #pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(n)

def read_json(s):
    with open("Alarm.json","r") as f:
        alarmData=json.load(f)
    return alarmData[s]

#Alarm and reminders
def ring_alarm(x):
    if (x=="a") and (awake==False):
        play_audio("Voices/Okitemasuka.wav",3)
    if (x=="s") and (awake==False):
        play_audio("Voices/Okite.wav",5)
def reminder(x):
    if x=="22":
        play_audio("Voices/2200.wav",0)
    if x=="23":
        play_audio("Voices/2300.wav",0)
#init
pygame.init()
pygame.mixer.init()
awake = False
host='localhost'
port=10500
DATASIZE=1024

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,port))

res=""
fin_flag=False

def alarm():
    while True:
        print(datetime.now().strftime("%H:%M"))
        if datetime.now().strftime("%H:%M")==read_json("alarm"):
            ring_alarm("a")
        if datetime.now().strftime("%H:%M")==read_json("snooze"):
            ring_alarm("s")
        if datetime.now().strftime("%H:%M")=="22:00":
            reminder("22")
        if datetime.now().strftime("%H:%M")=="23:00":
            reminder("23")
        time.sleep(60)

ThreadPoolExecutor().submit(alarm)

while True:
    data = sock.recv(DATASIZE).decode("utf-8")
    for line in data.split('\n'):
        index=line.find('WORD=')
        if index != -1:
            res = res + line[index+6:line.find('"',index+6)]
        if '</RECOGOUT>' in line:
            fin_flag=True
    if fin_flag==True:
        if "おはよう" in res:
            if awake:
                print(awake)
            pygame.mixer.music.stop()
            if not awake:
                awake = True
                if datetime.strptime(datetime.now().strftime("%H:%M"),"%H:%M")<datetime.strptime("11:00","%H:%M"):
                    play_audio("Voices/Ohayou.wav",0)
                else:
                    play_audio("Voices/konnnichiwa.wav",0)
                slackbot.morning()
        if "おやすみ" in res:
            awake = False
            play_audio("Voices/Oyasumi.wav",0)
            slackbot.slept()
        if "いってきます" in res:
            play_audio("Voices/Itterassyai.wav",0)
            slackbot.gone()
        if "ただいま" in res:
            play_audio("Voices/okaeri.wav",0)
            slackbot.returned()
        fin_flag=False
        res=""
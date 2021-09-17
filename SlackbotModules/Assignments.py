import os
import urllib.request
import requests
from bs4 import BeautifulSoup

def GetAssignments():
    #Login
    username=os.environ[PANDA_USERNAME]
    password =os.environ[PANDA_PASSWORD]
    payload={
        "username":username,
        "password":password
    }
    sess = requests.Session()
    url_login = "https://cas.ecs.kyoto-u.ac.jp/cas/login?service=https%3A%2F%2Fpanda.ecs.kyoto-u.ac.jp%2Fsakai-login-tool%2Fcontainer"
    res_login = sess.get(url_login)
    text_login = BeautifulSoup(res_login.text)
    lt = text_login.find(attrs={'name': 'lt'}).get('value')
    execution = text_login.find(attrs={'name': 'execution'}).get('value')
    _eventId = text_login.find(attrs={'name': '_eventId'}).get('value')
    payload['lt'] = lt
    payload['execution'] = execution
    payload['_eventId'] = _eventId
    res_home=sess.post(url_login,data=payload)

    #Retrieve .json
    url_json="https://panda.ecs.kyoto-u.ac.jp/direct/assignment/my.json"
    urllib.request.urlretrieve(url_json,"assignments.json")

    #message
    message="*課題*\n"
    message+="なし!"
#GetAssignments()
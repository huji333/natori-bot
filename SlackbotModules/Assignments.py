import os
import urllib.request
import requests
import json
from bs4 import BeautifulSoup

def get_assignments():
    #Login
    username=os.environ["PANDA_USERNAME"]
    password =os.environ["PANDA_PASSWORD"]
    payload={
        "username":username,
        "password":password
    }
    sess = requests.Session()
    url_login = "https://panda.ecs.kyoto-u.ac.jp/cas/login?service=https%3A%2F%2Fpanda.ecs.kyoto-u.ac.jp%2Fsakai-login-tool%2Fcontainer"
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
    with open("assignments.json","r",encoding="UTF-8") as f:
        assignments_data=json.load(f)

    print(len(assignments_data["assignment_collection"]))
    #message
    message="\n*課題*\n"
    if len(assignments_data["assignment_collection"])==0:
        message+="なし!"
    else:
        for i in range(len(assignments_data["assignment_collection"])):
            duedt = datetime.strptime(assignments_data["assignment_collection"][i]["dueTimeString"],"%Y-%m-%dT%H:%M:%SZ")
            due = datetime.strftime(duedt,"%m/%d %H時")
            message+=(">"+assignments_data["assignment_collection"][i]["title"]+"　締切:"+due+"\n")
    return message
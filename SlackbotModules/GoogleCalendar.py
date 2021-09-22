from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import timedelta
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_events(): 
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    tdy = datetime.datetime.utcnow()+timedelta(hours=18)
    endt = tdy.isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        timeMax=endt, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    #message
    message = "\n*予定*\n"
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        message+=(">"+start[11:15]+" "+event['summary']+"\n")
    return message

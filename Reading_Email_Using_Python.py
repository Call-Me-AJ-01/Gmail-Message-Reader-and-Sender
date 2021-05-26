import os
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.message import EmailMessage
import smtplib
import pyttsx3 as r
engine = r.init()
engine.setProperty('rate',140)
def speak(text):
    engine.say(text)
    engine.runAndWait()
import socket
import random
import speaker as sp
global c1
c1=0
ii=0
k=0
t=0
res=["hai sir","hello sir","sir"]
while True:
    try:
        if socket.create_connection(('google.com',80)):
            speak("initializing Gmail reader from aj mark 2")
            break
    except:
        if t==0:
            speak("system is not connected to internet")
            speak("please connect the system to internet in order to activate gmail reader from aj mark 2")
            t+=1
def gmail():
    try:
        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        i,c=0,0
        if i==0:
            creds = None
            if os.path.exists('token.pickle'):#path of token with "/" slash
                with open('token.pickle', 'rb') as token:# path of token with "/" slash
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)#path of credentials with "/" slash
                    creds = flow.run_local_server(port=0)
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            print('1')
            service = build('gmail', 'v1', credentials=creds)
            results=service.users().messages().list(userId='me',labelIds=['INBOX']).execute()
            messages=results.get('messages',[])
            for message in messages[:1]:
                p_msg=service.users().messages().get(userId='me',id=message['id']).execute()
                headers=p_msg["payload"]["headers"]
                p_subject= [i['value'] for i in headers if i["name"]=="Subject"]
                headers=p_msg["payload"]["headers"]
                From= [i['value'] for i in headers if i["name"]=="From"]
                From=str(From).split("<")
                from_=From[0]
                p_from_=from_.replace("['","")
                from_id=From[1]
                p_from_id=from_id.replace(">']","")
                i+=1
        while True:
            creds = None
            if os.path.exists('token.pickle'):#path of token with "/" slash
                with open('token.pickle', 'rb') as token:# path of token with "/" slash
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)#path of credentials with "/" slash
                    creds = flow.run_local_server(port=0)
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            service = build('gmail', 'v1', credentials=creds)
            results=service.users().messages().list(userId='me',labelIds=['INBOX']).execute()
            messages=results.get('messages',[])
            for message in messages:
                msg=service.users().messages().get(userId='me',id=message['id']).execute()
                headers=msg["payload"]["headers"]
                subject= [i['value'] for i in headers if i["name"]=="Subject"]
                headers=msg["payload"]["headers"]
                From= [i['value'] for i in headers if i["name"]=="From"]
                From=str(From).split("<")
                from_=From[0]
                from_=from_.replace("['","")
                try:
                    from_id=From[1]
                except:
                    from_id=From[0]
                from_id=from_id.replace(">']","")
                if from_id==p_from_id and subject==p_subject:
                    break
                else:
                    if i==1:
                        p1_from_id=from_id
                        p1_subject=subject
                        i+=1
                    c+=1
            for message in messages[:c]:
                msg=service.users().messages().get(userId='me',id=message['id']).execute()
                headers=msg["payload"]["headers"]
                subject= [i['value'] for i in headers if i["name"]=="Subject"]
                headers=msg["payload"]["headers"]
                From= [i['value'] for i in headers if i["name"]=="From"]
                From=str(From).split("<")
                from_=From[0]
                from_=from_.replace("['","")
                try:
                    from_id=From[1]
                except:
                    from_id=From[0]
                from_id=from_id.replace(">']","")
                #print("From :",from_)
                #print("Id :",from_id)
                #print("subject:"+str(subject[0]))
                #print("Message:"+str(msg['snippet']).strip())
                if len(str(msg['snippet']).strip())<1:
                    msg['snippet']="Some kind of files or documents are attached"
                speak(random.choice(res)+" , you have a new Mail from ---"+str(from_))
                if len(str(subject[0]))<1:
                    speak("this mail has no subject")
                else:
                    sp.speak_msg("regarding , "+subject[0])
                speak("moving on to the content of the mail")
                sp.speak_msg(str(msg['snippet']).replace("&#39;",""))
            if c!=0:
                p_from_id=p1_from_id
                p_subject=p1_subject
            c=0
            i=1
    except:
        ii=0
        while True:
            try:
                if socket.create_connection(('google.com',80)):
                    if ii==1:
                        speak("reconnected to internet")
                        speak("Activating Gmail reader from aj mark 2")
                        gmail()
                        break
                    else:
                        gmail()
                        break
            except:
                if ii==0:
                    speak("Internet disconnected, please connect to the internet , to activate gmail reader from AJ Mark 2")
                    ii+=1
        
gmail()
print('end')

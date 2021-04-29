import pyttsx3
import speech_recognition as sr          # https://realpython.com/python-speech-recognition/  https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
import datetime
import time
import os
import cv2
import random
import wikipedia
import webbrowser
import smtplib
import sys
import pyjokes
import mime
import pyautogui                  #  control the mouse and keyboard, and other GUI automation tasks. For Windows, macOS, and Linux, on Python 3 and 2.
import requests
import pywhatkit as kit
from requests import get

# modules for email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
#  for gui
from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovies
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)   
engine.setProperty('voices', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into twxt
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:    #for taking command from user
        print("Listening...")
        r.pause_threshold = 1           # i modify pause_threshold coz if i take a gap in speaking then my jarvis can't stop.
        audio = r.listen(source)        # audio = r.listen(source, timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "none"
    return query 

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i m jarvis sir. Please tell me how can i help you")


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('techsterapp@gmail.com', 'chaudhary007')   
    server.sendmail('s.shivu007007@gmail.com', to, content)
    server.close

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=78e7d08b755d49498b0e0657ad8e9d6b'
   
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"{head[i]}")


if __name__ == "__main__":
    # speak("hi i'm jarvis")
    wish()
    while True:
    # if 1:
        query = takeCommand().lower()

        # logic building for tasks
        if 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        
        elif 'open wps' in query:
            wpsPath = "C:\\Users\\user\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe"
            os.startfile(wpsPath)
        
        elif 'open cmd' in query:
            os.system('start cmd')
        
        # """
        # elif 'open camera' in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam', img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break
        # """            
        elif 'play music' in query:
            music_dir = "D:\\songs\\slow somg" 
            songs = os.listdir(music_dir)
            # print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'jarvis what is my ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            # print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            # speak('sir, what shoud i play on youtube')
            # cm = takeCommand
            # kit.playonyt(f"{cm}")


        elif 'open google' in query:
            speak('sir, what should i search on google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'email to shivani' in query:
            
            speak("sir what should i say?")
            query = takeCommand().lower()

            if "send a file" in query or 'send file' in query:
                email = 'techsterapp@gmail.com'
                password = 'chaudhary007'
                send_to_email = 's.shivu007007@gmail.com'
                speak('okay sir, what is the subject for this email')
                query = takeCommand().lower()
                subject = query
                speak('and sir, what is the message for this email')
                query2 = takeCommand().lower()
                message = query2
                speak('sir please enter the correct path of the file into the shell')
                file_location = input('please enter the path here: ')

                speak('please wait, i am sending email now')

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

                # attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to shivani")

            else:
                email = 'techsterapp@gmail.com'
                password = 'chaudhary007'
                send_to_email = 's.shivu007007@gmail.com'
                message = query               
               
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to shivani")


            # try:
            #     speak('what should i say?')
            #     content = takeCommand().lower()
            #     to = "s.shivu007007@gmail.com"
            #     sendEmail(to,content)
            #     speak('Email has been sent to shivani')

            # except Exception as e:
            #     print(e)
            #     speak("sorry sir, i'm not able to snet this email")

        elif 'close not paid' in query:
            speak('okay sir, closing notepad')
            os.system("taskkill /f /im notepad.exe")

        # elif 'close wps' in query:
        #     speak('okay sir, closing wps office')
        #     os.system("taskkill /f /im ksolaunch.exe    ")

    # to find joke
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

    # to listen news
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

    # to working on system
        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'no you can sleep' in query:
            speak('thanks for using me sir, have a good day.')
            sys.exit()
        
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak('sir, please tell me the name for this screenshot file.')
            name = takeCommand().lower()
            speak('i am taking screenshot')
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f'{name}.png')
            speak('i am done sir, now i am ready for next command')

        # -------------- to hide files of folder --------------- #
        elif 'hide all files' in query or 'hide this folder' or 'visible for everyone' in query:
            speak('sir please tell me you want to hide this folder or make it visible for everyone')
            condition = takeCommand().lower()
            
            if 'hide' in condition:
                os.system('attrib +h /s /d')
                speak('sir, all the files in this folder are now hidden')

            elif 'visible' in condition:
                os.system('attrib -h /s /d')
                speak('sir, all the file in this folder are now visible for everyone. i wish you are taking this decision in your own peace.')

            elif 'leave it' in condition or 'leave for now' in condition:
                speak('ok sir')
                

    # to chech instagram profile
        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak('sir please enter the username correctly.')
            name = input('enter username here: ')
            webbrowser.open(f'www.instagram.com/{name}')
            speak(f'sir here is the profile of the user{name}')
    ################################################################################################################
            # coding for downlaod instagram profile picture 
            # time.sleep(5)
            # speak('sir would you like to download profile picture of this account?')
            # condition = takeCommand.lower()
            # if 'yes' in condition:
            #     mod = instaloader.instaloader()
            #     mod.download_profile(name, profile_pic_only=True)
            #     speak('i am done sir, profile picture is saved. now i am ready for next command')
            # else:
            #     pass
    ##################################################################################################################

        speak("sir, do you have any other work?")

        

        # elif 'send message' in query:
        #     kit.sendwhatmsg("+918866944108", "Hi, i'm Darshil",15,56)
  
    # youtube_play()
    takeCommand()

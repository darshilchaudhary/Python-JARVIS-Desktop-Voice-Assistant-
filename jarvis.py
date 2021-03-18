"""
pyttsx is a cross-platform text to speech library which is platform independent. 
The major advantage of using this library for text-to-speech conversion is that it works offline. 
However, pyttsx supports only Python 2.x. Hence,
we will see pyttsx3 which is modified to work on both Python 2.x and Python 3.x with the same code.
https://www.geeksforgeeks.org/python-text-to-speech-pyttsx-module/
""" 



import pyttsx3
import speech_recognition as sr        # https://realpython.com/python-speech-recognition/  https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
import datetime
import wikipedia
import webbrowser
import os
import smtplib                      # for sending mails


engine = pyttsx3.init('sapi5')          # sapi5(Speech Application Programming Interface) is Microsoft speech API   https://en.wikipedia.org/wiki/Microsoft_Speech_API
voices = engine.getProperty('voices')   # to get voices from system 
print(voices[0].id)                     
engine.setProperty('voice',voices[0].id)    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("goof afternoo!")

    else:
        speak("good evening!")

    speak("i m jarvis sir. Please tell me how may i help you")


def takeCommand():                      # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    # i modify pause_threshold coz if i take a gap in speaking then my jarvis can't stop.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(do, content):                    #we use smtplib module for sending mails through gmail
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('techsetrapp@gmail.com', 'chaudhary007')
    server.sendmail('techsterapp@gmail.com', to, content)
    server.close


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    # speak("darshil is a good boy")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\\songs\\slow somg" 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open wps' in query:
            wpsPath = "C:\\Users\\user\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe"
            os.startfile(wpsPath)

        elif 'send email to shivani' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "s.shivu007007@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir, i m not able to send this email")



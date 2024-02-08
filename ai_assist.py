import pyttsx3
import datetime
import pyaudio
import wikipedia
import os
import pyautogui
import psutil
import  speech_recognition as sr
import webbrowser as wb
engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    t=datetime.datetime.now().strftime("%H : %M : %S")
    speak("The current time is ")
    speak(t)
def date():
    d=datetime.datetime.now().day
    m=datetime.datetime.now().month
    y=datetime.datetime.now().year
    speak("The current date is ")
    speak(d)
    speak(m)
    speak(y)
def wish():
    name=input()
    hour = datetime.datetime.now().hour
    if hour >= 6  and hour < 12:
        speak("Good Morning "+ name)
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon "+ name)
    elif hour >= 16 and hour < 20:
        speak("Good Evening "+ name)
    elif hour >= 20 and hour < 24:  
        speak("Good Night "+ name)
    elif hour >= 0 and hour < 6:  
        speak("Good Night "+ name)
    
    time()
    date()
def com():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        audio=r.listen(source)
        
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say again please!!")
        return "None"
    return query
def screenshot():
    img=pyautogui.screenshot()
    img.save()
def cpu():
    usage=str(psutil.cpu_percent())
    speak('usage is '+ usage)
    battery=psutil.sensors_battery()
    speak('Battery is at ')
    speak(battery.percent)
    speak('percentage')
if __name__ == "__main__":
    wish()
    while True:
        query = com().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'google chrome' in query:
            speak("What should I search?")
            chpath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search=com().lower()
            wb.get(chpath).open_new_tab(search+'.com')
        elif 'logout' in query:
            speak('System Logout')
            os.system('shutdown -1')
        elif 'restart' in query:
            speak('System restarting')
            os.system('shutdown \r \t 1')
        elif 'shutdown' in query:
            speak('System Shutdowning')
            os.system('shutdown \s \t 1')
        elif 'remember' in query:
            speak('What should I remeber?')
            data=com()
            speak('Is it '+ data)
            temp=com()
            if 'yes' in temp:
                remember=open('data.txt','w')
                remember.write(data)
                remember.close()
            else:
                speak('Say again')
        elif 'saved notes' in query:
            remember=open('data.txt','r')
            speak(remember.read())
        elif 'Screenshot' in query:
            screenshot()
            speak('Screen shot Done!')
        elif 'CPU' in query:
            cpu()
        elif 'stop' in query:
            speak("System going offline")
            quit()
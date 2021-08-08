import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser#pip install webbrowser but noneed inbuilt
import os
import smtplib #mail
import subprocess 
import shutil
import winshell
import ctypes
from ecapture import ecapture as ec
import pywhatkit
import time

engine = pyttsx3.init('sapi5')
#including the voices
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)


def speak(audio):#acess
    engine.say(audio)
    engine.runAndWait()

def acess():#Acess
    acess="Tushar"
    speak("who are you")
    acess=takeCommand()
    if acess=="Tushar":
        speak("acess granted")
    elif acess!="Tushar":
        speak("acess denied")
        raise SystemExit


def TaskExe():
    print("Hello I Am a Virtual Assistant created by Tushar")
    speak("Hello I Am a Virtual Assistant created by Tushar")
    print("How can I help you")
    speak("How can I help you")
    print('But!!!,Before That Let me Confirm The Password')
    speak('But!!!,Before That Let me Confirm The Password')
    


    
        
    

#def greet():
 #   speak("could you please tell your name")
  #  takeCommand()
def wishMe():#wish me
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Version 2 point o")  

def usrname():
    speak("what should i call you")
    uname=takeCommand()
    speak('Welcome')
    speak(uname)
    
    print("Welcome Mr.", uname)
    
     
    speak("How can i Help you, Sir")   

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
def Music():
    speak("Which song do you want to listen")
    musicname = takeCommand()
    if 'ankon' in musicname:
        os.startfile('C:\\Users\\lenovo\\Music\\ankon.mp3')
    else:
        pywhatkit.playonyt(musicname)
        speak("Enjoy!!")
def Whatsapp():
    speak("Tell me the name of the person")
    person=takeCommand()
    if 'Mahesh' in person:
        speak("What's the message")
        msg=takeCommand()
        speak("tell me the time")
        speak("time in hour")
        hour= int(takeCommand())
        speak("time in minutes")
        min=int(takeCommand())
        pywhatkit.sendwhatmsg("+919920463978",msg,hour,min)
        speak("Done sir!")

    elif 'home' in person:
        speak("What's the message")
        msg=takeCommand()
        speak("tell me the time")
        speak("time in hour")
        hour= int(takeCommand())
        speak("time in minutes")
        min=int(takeCommand())
        pywhatkit.sendwhatmsg("+917038146660",msg,hour,min)
        speak("Done sir!")


    else:
        speak("What's the number")
        phone=int(takeCommand())
        ph='+91'+phone
        speak("Tell the message")
        msg=takeCommand()
        speak("tell me the time")
        speak("time in hour")
        hour= int(takeCommand())
        speak("time in minutes")
        min=int(takeCommand())
        pywhatkit.sendwhatmsg(ph,msg,hour,min,1)
        speak("Done sir!")
def closeApps():
    if 'vs code' in query:
        os.system("TASKILL /F /in code.exe")
    elif 'chrome' in query:
        os.system("TASKILL /F /in chrome.exe ")
    elif 'turbo' in query:
        os.system("TASKILL /F /in turbo.in")
       
        

    

if __name__ == "__main__":
    TaskExe()
    acess()
    #greet()
    wishMe()
    usrname()
    while True:
        
        query = takeCommand().lower()

            # Logic for executing tasks based on query
        if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
        elif 'you need a break' in query:
            speak("Ok,You can call me anytime")
            speak("Just say Wake Up")
            raise SystemExit


        elif 'open youtube' in query:#youtube
                    webbrowser.open("youtube.com")
        elif 'open google' in query:#google
                    webbrowser.open("google.com")
        elif 'open music' in query:
            Music()
        elif 'open stackoverflow' in query:#stackoverflow
                    webbrowser.open("stackoverflow.com")   
        elif 'youtube search' in query:
            speak("which channel do you wanna visit")
            youtube=takeCommand()
            web='https://www.youtube.com/results?search_query='+ youtube
            webbrowser.open(web)
            speak("Done!")
        elif 'google search' in query:
            speak("This is what i found")
            query=query.replace("Jutastu","")
            query=query.replace("Google Search","")
            pywhatkit.search(query)
            speak("Done sir!")
        elif 'open website' in query:
            speak("which website do you want to launch")
            #speak("Ok sir! launching")
            google=takeCommand()
            web ="https://" +google+ '.com'
            webbrowser.open(web)
            #query=query.replace("Jutastu",)
            #query=query.replace("Search","")
            #web1= query.replace("open",google)
            #web2= 'https://www.' +web1 +'.com'
            #webbrowser.open(web2)
            speak("Done sir!")
        elif 'facebook profile' in query:
            speak("working on it")
            webbrowser.open('https://www.facebook.com/tushar.jaiswal.1276')
        elif 'facebook' in query:
            query=query.replace("jutatsu","")
            query=query.replace("Search","")
            web3=query.replace("open","")
            fb='https://www.facebook.com/' +web3
            webbrowser.open(fb)
        elif 'whatsapp' in query:
            Whatsapp()
        elif 'the time' in query:#date time
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
        elif 'open vscode' in query:#vscode
                    codePath ="C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
                    os.startfile(codePath)
        elif 'open qrcode' in query:
            Qrcode="C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\qrcode1\\demo.py"
            os.startfile(Qrcode)
        elif 'close chrome' in query:
            closeApps()
        elif 'close chrome' in query:
            closeApps()
        elif 'close turbo' in query:
            closeApps()
        elif "change name" in query:
                    speak("What would you like to call me, Sir ")
                    assname = takeCommand()
                    speak("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
                    speak("My friends call me")
                    speak(assname)
                    print("My friends call me", assname)
        elif 'email to Tushar' in query:#mail
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "tushar.08j@gmail.com"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend Tushar bhai. I am not able to send this email")  
        elif "don't listen" in query or "stop listening" in query:
                    speak("for how much time you want to stop jarvis from listening commands")
                    a = int(takeCommand())
                    time.sleep(a)
                    print(a)
        elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        elif "camera" in query or "take a photo" in query:
                    ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("Are u sure")
            reply=takeCommand()
            if 'yes' in reply:
                os.system("shutdown /s /t 1")
            else:
                raise SystemExit

        elif "restart" in query:
            speak("Are u sure")
            reply=takeCommand()
            if 'yes' in reply:
                os.system("shutdown /r /t 1")
            else:
                raise SystemExit

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            speak("Are u sure")
            reply=takeCommand()
            if 'yes' in reply:
                os.system("shutdown /h /t 1")
            else:
                raise SystemExit

        elif "log off" in query or "sign out" in query:
            time.sleep(2)
            speak("Make sure all the application are closed before sign-out")
            speak("Are u sure")
            reply=takeCommand()
            if 'yes' in reply:
                os.system("shutdown /l /t 1")
            else:
                raise SystemExit
    
    
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
    
        elif 'Exit' in query: #exit
            speak("Hope to see you soon")
            print("Have a nice day")

def end():
    speak("have a nice day")
    print("thank you")

if __name__=="__main__":
    end()
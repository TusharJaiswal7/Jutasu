import speech_recognition as sr
import os



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

while True:
    Wake_Up=takeCommand()
    if 'wake up Jarvis'in Wake_Up:
        os.startfile('C:\\Users\\lenovo\\OneDrive\\Desktop\\project\\Jarvis\\jutasu.py')
        #python jutasu.py
    else:
        print("Not Found")
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am aidva. How may i help you?")

def takeCommand():
    '''
    It takes microphone input from the user and returns string as output.
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rishaviitian811311@gmail.com', 'Rish130"&')
    server.sendmail('rishaviitian811311@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...') 
            query=query.replace("wikipedia", "")
            try:
                results=wikipedia.summary(query, sentences=1)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print("Not found... Try again...")
                speak("Not found... Try again...")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Rishali Kumari\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            x=random.randrange(0,len(songs))
            os.startfile(os.path.join(music_dir, songs[x]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\Rishali Kumari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Rishav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "2019130@iiitdmj.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Rishav. I am not able to send this email")
        
        elif 'stop' in query:
            speak('Thank You!!! Hope to meet soon!!!')
            exit()
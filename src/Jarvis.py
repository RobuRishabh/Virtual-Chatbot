import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)      #it will give hour in int
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak("Hello!,Mr.Singh. I am Jarvis. Please tell me how may I help you")

def takeCommand():
    '''
    #It takes microphones input from the user and returns string output
    '''
    r = sr.Recognizer()  #this class will help to recognize our voice
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:          #if any error occured or google is not able to verify then Exception will run it will return None
        print(e)

        print("Say that again please...")
        return  "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open Stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'https://www.youtube.com/playlist?list=PL4A029DE14CB39A57'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'email to' in query:
            try:
                speak("What should I say in the email?")
                content = takeCommand()
                to = "jha.rau@northeastern.edu"
                sendemail(to, content)
                speak("Your email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, Mr.Singh. I was not able to send your email")





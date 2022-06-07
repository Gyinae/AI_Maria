import speech_recognition as sr
import pyttsx3
import pyaudio
import pyjokes
import pywhatkit
import wikipedia
from flask import Flask
import datetime
import webbrowser
import os
import smtplib



listener = sr.Recognizer()
Maria = pyttsx3.init()
voices = Maria.getProperty("voices")
Maria.setProperty("voice", voices[1].id)

def talk(text):
    Maria.say(text)
    Maria.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("I am Maria, how may I help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your_password')
    server.sendmail('your email', to, content)
    server.close()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "maria" in command:
                command = command.replace("maria", "")
                talk(f" you said: {command}\n")
    except:
        pass
    return command

def run_maria():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace("play", "")
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("the current time is" + time)

    elif "who is" in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "date" in command:
        talk(datetime.datetime.now().date())

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open linkedin" in command:
        webbrowser.open("linkedin.com")

    elif "open twitter" in command:
        webbrowser.open("twitter.com")

    elif 'open stackoverflow' in command:
        webbrowser.open("stackoverflow.com")

    elif 'music' in command:
        music_dir = 'D:\music\Spillage Village - Spilligion (2020) Mp3 320kbps [PMEDIA] ⭐️'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[1]))

    elif 'email to Samuel' in command:
        try:
            talk("What should I say?")
            content = take_command()
            to = "email"
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry my Samuel. I am not able to send this email")


wishMe()
while True:
    run_maria()

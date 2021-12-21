import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("time right now is")
    speak(Time)




def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("and the current date is")
    speak(date)
    speak(month)
    speak(year)



def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("good evening")
    else:
        speak("good night")
    speak("Dark at your service sir, How can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak(" i didn't get it can you please reapeat")

        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("dkkurre5@gmail.com", "Dkkurre@12")
    server.sendmail("dkkurre5@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Dk/Pictures/ss/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at" + usage)

    battery = psutil.sensors_battery
    speak("battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()


        elif "send mail" in query:
            try:
                speak("what will be in mail?")
                content = takeCommand()
                to = "dkkurre2050@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send the message")

        elif "wikipedia" or "tell me" or "what is" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak(result)

        elif "search in chrome" or "open chrome"  in query:
            speak("What should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")



        elif "thankyou" in query:
            speak("glad to help you")

        elif "offline" or "stop" in query:
            quit()

        elif "logout" in query:
            os.system("shutdown -1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember" + remember.read())

        elif "take screenshot" in query:
            screenshot()
            speak("done")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()
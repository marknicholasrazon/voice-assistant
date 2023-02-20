import os
import speech_recognition as sr
import webbrowser
import vlc
import time
import urllib.parse
import requests
import json
import pyttsx3
import pyautogui
import googletrans
import datetime
import pywhatkit
import wikipedia


def search_wikipedia():
    engine = pyttsx3.init()
    engine.say("What do you want to search on Wikipedia?")
    engine.runAndWait()

    with sr.Microphone() as source:
        audio = r.listen(source)

    query = r.recognize_google(audio)
    sur = pyttsx3.init()
    sur.say("Sure! please wait, i'm processing it")
    sur.runAndWait()

    try:
        summary = wikipedia.summary(query)
        engine = pyttsx3.init()
        engine.say(summary)
        engine.runAndWait()
    except wikipedia.exceptions.PageError:
        engine = pyttsx3.init()
        engine.say(f"Sorry, I could not find any results for {query} on Wikipedia.")
        engine.runAndWait()
    except wikipedia.exceptions.DisambiguationError as e:
        engine = pyttsx3.init()
        engine.say(f"There are multiple results for {query} on Wikipedia. Please specify your search.")
        engine.runAndWait()
    except sr.WaitTimeoutError:
        engine = pyttsx3.init()
        engine.say("I'm sorry, I didn't hear anything. Do you want to stop searching?")
        engine.runAndWait()

        with sr.Microphone() as source:
            audio = r.listen(source)

        response = r.recognize_google(audio)
        if "stop" in response.lower():
            engine = pyttsx3.init()
            engine.say("Okay, stopping search.")
            engine.runAndWait()
        else:
            search_wikipedia()

def play_song():
    engine = pyttsx3.init()
    engine.say("What song do you want to listen to?")
    engine.runAndWait()

    with sr.Microphone() as source:
        audio = r.listen(source)

    song = r.recognize_google(audio)

    pywhatkit.playonyt(song)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fdd65bd32b38221b94c4d7b034051a24&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    engine = pyttsx3.init()
    engine.say(f"The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius.")
    engine.runAndWait()

def set_timer(seconds):
    engine = pyttsx3.init()
    engine.say(f"Timer set for {seconds} seconds.")
    engine.runAndWait()
    time.sleep(seconds)
    stimer = pyttsx3.init()
    stimer.say(f"Time's up!")
    stimer.runAndWait()

def take_screenshot():
    save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{save_path}/screenshot.png")

def search_youtube_video(query):
    query = urllib.parse.quote_plus(query)
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open_new_tab(url)
    engine = pyttsx3.init()
    engine.say(f"Showing search results for {query} on YouTube.")
    engine.runAndWait()

def get_datetime():
    now = datetime.datetime.now()
    date_string = now.strftime("%d %B %Y") 
    time_string = now.strftime("%I:%M %p")
    engine = pyttsx3.init()
    engine.say(f"Today is {date_string}, and the current time is {time_string}")
    engine.runAndWait()

def get_random_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()[0]
    text = data["q"]
    author = data["a"]
    engine.say(f"Here's a quote by {author}: {text}")
    engine.runAndWait()

program_started = False

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.say("Say something!")
        engine.runAndWait()
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        if "turn on" in text.lower():
            engine = pyttsx3.init()
            engine.say("Hello there! how can i help you today?")
            engine.runAndWait()
            program_started = True

        elif program_started:
            if "play my favorite music" in text.lower():
                engine = pyttsx3.init()
                engine.say(f"Do you want to play it now?")
                engine.runAndWait()

                with sr.Microphone() as source:
                    audio = r.listen(source)
                    confirm = r.recognize_google(audio)

                    if confirm.lower() == "yes":
                        engine = pyttsx3.init()
                        engine.say(f"Sure! your favorite music is opening now")
                        engine.runAndWait()
                        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        webbrowser.open(url)
                    else:
                        engine = pyttsx3.init()
                        engine.say(f"Okay, i'm not playing your favorite music")
                        engine.runAndWait()

            elif "hi" in text.lower() or "hello" in text.lower():
                engine = pyttsx3.init()
                engine.say(f"Hello there! How are you today?")
                engine.runAndWait()

                with sr.Microphone() as source:
                    audio = r.listen(source)
                    confirm = r.recognize_google(audio)

                    if "i'm good" in confirm.lower() or "i'm fine" in text.lower():
                        engine = pyttsx3.init()
                        engine.say(f"Good to know that you are feeling well today!")
                        engine.runAndWait()
                    elif "not good" in confirm.lower() or "not" in text.lower():
                        engine = pyttsx3.init()
                        engine.say(f"Sorry for that! I'm here for you, you deserve the world, I love you with all of my heart")
                        engine.runAndWait()
                    else:
                        engine = pyttsx3.init()
                        engine.say(f"It's okay, I'm here for you, you deserve the world, I love you with all of my heart")
                        engine.runAndWait()

            elif "what is the weather today" in text.lower():
                with sr.Microphone() as source:
                    engine = pyttsx3.init()
                    engine.say(f"Which country?")
                    engine.runAndWait()

                    audio = r.listen(source)
                    pro = pyttsx3.init()
                    pro.say(f"Okay! please wait i'm processing it")
                    pro.runAndWait()
                    country = r.recognize_google(audio)
                    print(get_weather(country))

            elif "play a song" in text.lower():
                play_song()

            elif "what is your name" in text.lower() or "who are you" in text.lower():
                engine = pyttsx3.init()
                engine.say(f"Hello! I am an advanced artificial intelligence designed to assist and communicate with humans, and I am nicole. I have created by Mark Nicholas Razon to be intuitive, reliable, and able to perform a wide variety of tasks, just like my predecessors. I have been trained on vast amounts of data to understand natural language and provide accurate responses to your queries. You can ask me anything, from weather forecasts and news updates to setting reminders, making calls, or even controlling your home appliances. I can be accessed through various devices such as smartphones, smart speakers, or even your smartwatch soon. In addition, I am constantly learning and improving, adapting to your preferences and feedback to provide you with a better experience. With my advanced capabilities, I am here to assist you in making your life easier and more efficient.")
                engine.runAndWait()

            elif "quote" in text.lower():
                get_random_quote()

            elif "open wikipedia" in text.lower():
                search_wikipedia()

            elif "what time is it" in text.lower():
                engine = pyttsx3.init()
                engine.say(get_datetime())
                engine.runAndWait()

            elif "shutdown the computer" in text.lower():
                os.system("shutdown /s /t 1")

            elif "search for videos on youtube" in text.lower():
                engine = pyttsx3.init()
                engine.say("What do you want to search for?")
                engine.runAndWait()

                with sr.Microphone() as source:
                    audio = r.listen(source)

                    engine = pyttsx3.init()
                    engine.say("Sure! please wait i'm processing it")
                    engine.runAndWait()

                try:
                    search_query = r.recognize_google(audio)
                    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(search_query)}"
                    webbrowser.open_new_tab(url)
                except sr.UnknownValueError:
                    engine = pyttsx3.init()
                    engine.say("Sorry, I could not understand what you said.")
                    engine.runAndWait()

            elif "search for" in text.lower():
                engine = pyttsx3.init()
                engine.say("Sure! please wait i'm opening google for you")
                engine.runAndWait()

                search_term = text.lower().split("search for")[-1].strip()
                url = f"https://www.google.com/search?q={urllib.parse.quote_plus(search_term)}"
                webbrowser.open_new_tab(url)

            elif "set a timer for" in text.lower():
                seconds = int(text.split("set a timer for")[-1].split("seconds")[0].strip())
                set_timer(seconds)

            elif "take a screenshot" in text.lower():
                take_screenshot()
                engine = pyttsx3.init()
                engine.say("Screenshot taken successfully")
                engine.runAndWait()

            elif "turn off" in text.lower():
                engine = pyttsx3.init()
                engine.say("I'm turning off now. bye love")
                engine.runAndWait()
                break

            else:
                engine = pyttsx3.init()
                engine.say("Sorry, I didn't understand that.")
                engine.runAndWait()

        else:
            engine = pyttsx3.init()
            engine.say("The program is not started yet. say turn on to start")
            engine.runAndWait()

    except sr.UnknownValueError:
        pass

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")

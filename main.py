import os
import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
from google import genai
from config import apikey
import re

def ai(prompt):
    client = genai.Client(api_key=apikey)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_text = response.text
    print(ai_text)

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # Remove trigger words
    query_text = prompt.replace("artificial intelligence", "").strip()

    # Fallback filename
    if not query_text:
        query_text = "general_query"

    # Windows-safe filename
    safe_filename = re.sub(r'[\\/:*?"<>|]', '', query_text)

    filepath = f"Openai/{safe_filename}.txt"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(ai_text)


def say(text):
    engine = pyttsx3.init()     # create new engine each time
    engine.setProperty("rate", 160)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        return ""

if __name__ == "__main__":
    say("  Jarvis AI")

    while True:
        query = takecommand()
        #time.sleep(0.3)  # allow audio engine to release mic
        #todo: Add more sites
        sites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "wikipedia": "https://www.wikipedia.com"
        }

        for name, url in sites.items():
            if f"open {name}" in query:
                say(f"Opening {name} sir")
                webbrowser.open(url)

        #todo: Add a feature to play a specific song

        if "open music" in query:
            musicpath = r"C:\Users\Zeeshan\Downloads\Video\123.mp4"
            if os.path.exists(musicpath):
                say("Opening music sir")
                os.startfile(musicpath)
            else:
                say("Music file not found")

        if "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")

        if "notes" in query:
            filepath = r"C:\5th Semester"
            say("Opening Notes Sir")
            os.startfile(filepath)

        if "artificial intelligence" in query:
            ai(prompt = query)





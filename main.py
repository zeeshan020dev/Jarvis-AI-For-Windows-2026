import speech_recognition as sr
import os
import re
import datetime
import webbrowser
import pyttsx3
from google import genai
from config import apikey

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# ------------------- AI FUNCTIONS -------------------
client = genai.Client(api_key=apikey)

chatStr = ""

def chat(query: str):
    global chatStr

    if not query.strip():
        return

    chatStr += f"User: {query}\nJarvis: "

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=chatStr
        )
    except ClientError as e:
        handle_api_error(e)
        return

    ai_text = response.text.strip()
    chatStr += ai_text + "\n"

    print(ai_text)
    say(ai_text)


def ai(prompt: str):
    if not prompt.strip():
        return

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
    except ClientError as e:
        handle_api_error(e)
        return

    ai_text = response.text.strip()
    print(ai_text)
    say(ai_text)

    os.makedirs("Openai", exist_ok=True)

    clean_prompt = prompt.replace("artificial intelligence", "").strip()
    safe_name = re.sub(r'[\\/:*?"<>|]', '', clean_prompt) or "general_query"

    with open(f"Openai/{safe_name}.txt", "w", encoding="utf-8") as f:
        f.write(ai_text)

# -------------------- ERROR HANDLER --------------------
from google.genai.errors import ClientError
import time


def handle_api_error(error: ClientError):
    error_code = getattr(error, "code", None)

    if error_code == 429:
        print("⚠️ Gemini API quota exhausted")
        say("Sir, my free Gemini quota is exhausted. Please wait a moment.")

        # Respect retry delay if provided
        retry_delay = 3
        try:
            retry_info = error.details[2]
            retry_delay = int(retry_info.get("retryDelay", "3s").replace("s", ""))
        except Exception:
            pass

        time.sleep(retry_delay)

    else:
        print("❌ Gemini API error:", error)
        say("Sir, an error occurred while contacting the AI.")


# ------------------- SPEECH INPUT -------------------
def take_command() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

# ------------------- MAIN LOOP -------------------
if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis AI Activated")
    while True:
        print("Listening...")
        query = take_command()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query.lower():
            musicpath = r"C:\Users\Zeeshan\Downloads\Video\123.mp4"
            if os.path.exists(musicpath):
                say("Opening music sir")
                os.startfile(musicpath)
            else:
                say("Music file not found")


        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")

        elif "artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""
            say(f"Sir, the chat has reset")

        else:
            print("Chatting...")
            chat(query)

# 🤖 Jarvis AI for Windows

A **voice-controlled personal AI assistant for Windows**, inspired by *JARVIS*, built using **Python**, **Google Gemini AI**, **Speech Recognition**, and **Text-to-Speech**.

Jarvis can:
- 🎙️ Listen to voice commands
- 🧠 Respond intelligently using **Google Gemini**
- 🔊 Speak responses aloud
- 🌐 Open websites
- 🎵 Play local music
- 📁 Open folders
- 📝 Save AI-generated responses
- ⏰ Tell the current time

---

## 🚀 Features

- **Voice Input** using microphone  
- **AI Conversations** powered by Google Gemini  
- **Text-to-Speech Output** (Jarvis speaks back)  
- **Website Automation** (Google, YouTube, Wikipedia)  
- **Local File & Music Access**  
- **Persistent Chat Memory**  
- **Error Handling for API Quotas**  

---

## 🛠️ Tech Stack

| Component | Technology |
|--------|------------|
| Language | Python 3.9+ |
| AI Model | Google Gemini (gemini-2.5-flash) |
| Speech Recognition | `SpeechRecognition` |
| Voice Output | `pyttsx3` |
| AI SDK | `google-genai` |
| OS | Windows |

---

## 📂 Project Structure

```text
Jarvis-AI-For-Windows/
│
├── main.py              # Main Jarvis AI logic
├── config.py            # API key configuration
├── Openai/              # Saved AI responses
├── .venv/               # Virtual environment
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
````

---

## 🔑 Prerequisites

Before running Jarvis, ensure you have:

* ✅ Python 3.9 or above
* ✅ A working microphone
* ✅ Internet connection
* ✅ Google Gemini API Key

---

## 🔐 Getting Google Gemini API Key (Step-by-Step)

1. Go to **Google AI Studio**
   👉 [https://aistudio.google.com/](https://aistudio.google.com/)

2. Sign in with your Google account

3. Click **“Get API Key”**

4. Create a new API key

5. Copy the key

---

## ⚙️ Configuration

### 1️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install speechrecognition pyttsx3 google-genai pyaudio
```

> ⚠️ If PyAudio fails on Windows, install using precompiled wheels:
> [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

### 2️⃣ Create `config.py`

```python
apikey = "YOUR_GEMINI_API_KEY_HERE"
```

⚠️ **Never commit your API key to GitHub**

---

## ▶️ Running Jarvis

```bash
python main.py
```

You should hear:

> **“Jarvis AI Activated”**

---

## 🎤 Supported Voice Commands

| Command                     | Action                |
| --------------------------- | --------------------- |
| Open Google                 | Opens Google          |
| Open YouTube                | Opens YouTube         |
| Open Wikipedia              | Opens Wikipedia       |
| Open Music                  | Plays local music     |
| Open Notes                  | Opens a folder        |
| What is the time            | Tells current time    |
| Artificial Intelligence ... | AI-generated response |
| Reset Chat                  | Clears chat memory    |
| Jarvis Quit                 | Exits the assistant   |

---

## 🧠 How AI Works

* Uses **Google Gemini (`gemini-2.5-flash`)**
* Maintains conversation context using `chatStr`
* Responses are spoken using **Text-to-Speech**
* Long AI responses are saved in the `Openai/` folder

---

## 🔊 Fix: Jarvis Not Speaking?

Ensure:

* ✔️ `pyttsx3` installed correctly
* ✔️ System audio output is enabled
* ✔️ Windows speech engine is available

Test voice separately:

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("Testing Jarvis voice")
engine.runAndWait()
```

---

## 🐞 Common Errors & Fixes

### ❌ Microphone Timeout Error

```
speech_recognition.exceptions.WaitTimeoutError
```

✔️ Speak clearly
✔️ Ensure microphone access enabled
✔️ Reduce background noise

---

### ❌ API Quota Exhausted

Jarvis automatically:

* Detects `429` errors
* Waits before retrying
* Announces the issue via voice

---

## 🔒 Security Best Practices

* ❌ Do NOT hardcode API keys
* ✔️ Use `config.py` or environment variables
* ✔️ Add `config.py` to `.gitignore`

---

## 📌 Future Enhancements

* 🔐 Wake word detection
* 🌐 Offline mode
* 📱 Mobile integration
* 🧠 Memory persistence
* 🎯 Custom command training

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**[Muhammad Zeeshan Islam](https://github.com/zeeshan020dev)**
  
Co-Founder – [Unicodrex](https://www.linkedin.com/company/unicodrex/) | Technical Lead – [Skill Sprint](https://www.linkedin.com/company/skill-sprint-pk/) | Unity Game Developer – [CEGA](https://www.linkedin.com/company/cegaofficialpk/)

<a href="https://github.com/zeeshan020dev">
  <img src="https://img.shields.io/badge/GitHub-zeeshan020dev-ffffff?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117" />
</a>


---

## ⭐ Support

If you like this project, please ⭐ star the repository and share it!

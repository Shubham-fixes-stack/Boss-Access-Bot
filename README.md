# 🤖 Boss-Access-Bot (Module 1)

Welcome to the foundation of **Project Jarvis 2.0**! This Python module is an interactive security interface that combines **Text-to-Speech (TTS)** with conditional logic to create a "Voice-Enabled Guard" for your scripts.

## 🚀 Why this project?
I built this as a starting point for my upcoming AI assistant, **Jarvis 2.0**. It tests how a system can handle real-time user input while providing audio feedback, making the interaction feel more human and "Boss-like."

## ✨ Core Features (Based on Code)
* **Smart Authentication:** Uses a secure string comparison to grant access. Only the correct password triggers the "Boss" welcome sequence.
* **Hidden Numeric Tracker:** While the system is "Locked," it acts as a background calculator. If you enter numbers, it silently tracks and sums them up.
* **Real-time Voice Feedback:** Integrated with the `pyttsx3` engine to give:
    * Success greetings for the Admin.
    * Funny mocking alerts for unauthorized attempts.
    * Audio confirmation for every number added.
* **Anti-Spam Logic:** Includes a `time.sleep` delay for wrong attempts to prevent brute-force entries.

## 🛠 Tech Stack & Logic
* **Language:** Python 3.x
* **Primary Library:** `pyttsx3` (Cross-platform TTS)
* **Looping Logic:** Utilizes an infinite `while True` loop to maintain the system state until authorized.
* **Data Validation:** Uses `.isdigit()` to differentiate between potential passwords and numeric data.

## 📥 How to Run This Module
1.  **Install the Voice Engine:**
    ```bash
    pip install pyttsx3
    ```
2.  **Download & Launch:**
    Run the `main.py` file and interact with the bot through your terminal.
3.  **Secret Code:** Enter your password to unlock the final "Total Calculation" and the Boss Greeting.

---

### 📅 Road to Jarvis 2.0
- [x] Module 1: Voice Authentication & Basic Logic.
- [ ] Module 2: Voice Recognition (Listening to commands).
- [ ] Module 3: System Automation (Opening apps/files).

**Created for FUN and Learning by [Shubhamfixes](https://github.com/Shubham-fixes-stack)**

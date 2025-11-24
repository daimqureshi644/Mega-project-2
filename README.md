# Auto Chat Responder (Python • PyAutoGUI • Gemini API)

This project is an automated chat responder that reads chat messages from the screen, checks if the last message is from a specific sender, and then uses Google's Gemini API to generate and send a reply automatically.  
Useful for automating chat replies on platforms where API access is not available.

---

## 🚀 Features
- Reads on-screen chat using **PyAutoGUI**.
- Copies selected text using **clipboard automation**.
- Detects if the last message is from a specific sender.
- Generates a smart reply using **Gemini 2.0 Flash**.
- Pastes and sends the response automatically.

---

## 📦 Requirements
Install required libraries:

```bash
pip install pyautogui pyperclip google-generativeai

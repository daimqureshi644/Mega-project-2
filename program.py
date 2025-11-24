import pyautogui
import pyperclip
import time
import google.generativeai as genai


genai.configure(api_key="AIzaSyASZbzPPpBHYoxNkxHSwyKHviyI-hTeXzQ")


def is_last_message_form_sender(chat_log, sender_name = "Saify Petalnex"):
   messages = chat_log.strip().split("/2025] ")[-1]
   if sender_name in messages:
        return True
   return False

pyautogui.click(1486, 1040)
time.sleep(2)

while True:
    # Step 1: Click on chrome icon at cordinates (956, 1045)  
    # Step 2: Drag the mouse from (900, 289) to (1713, 902) to select the text
    pyautogui.moveTo(935, 281)
    pyautogui.dragTo(1854, 893, duration=1, button='left')

        # Step 3: Copy the selected text to the clip board
    pyautogui.hotkey("ctrl", 'c')
    pyautogui.click(1650, 930)
    time.sleep(2) # Wait for one second to ensure the copy command is completed
    # click to unselect the selected text

        # Step 4: Retrive the text from clipboard and store it in a variable 
    chat_history = pyperclip.paste()

        # Print the copied text to verify
    print(chat_history)

    if is_last_message_form_sender(chat_history):

        model = genai.GenerativeModel("gemini-2.0-flash")

        messages = model.generate_content([
            "You are a person name Daim Qureshi who speak urdu and english. You are from Pakistan. You analyze the chat hisory and respond like Daim, give short messages don,t give date and time",
            chat_history
        ])
    
        response_text = messages.text if hasattr(messages, "text") else str(messages)
        pyperclip.copy(response_text)

        pyautogui.click(1500, 947)
        time.sleep(1)


        pyautogui.hotkey("ctrl", 'v')
        time.sleep(1)

        pyautogui.press('enter')



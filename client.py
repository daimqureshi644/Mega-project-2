import google.generativeai as genai

client = genai (
   api_key= "api key"
)
command ='''
 hello

'''
completion = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role":"system","content":"You are a person name Daim Qureshi who speak urdu and english. You are from Pakistan. You analyze the chat hisory and respond like Daim",
        "role": "user","content":command}]
)

print(completion.choices[0].message.content)

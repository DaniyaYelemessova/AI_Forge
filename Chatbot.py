import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

url = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

history = []


def chat(message):
  history.append({
        "role": "user",
        "content": message
    })
  
  data = {
      "model": "openai/gpt-oss-120b:fastest",
      "messages": history
  }

  response = requests.post(
      url,
      headers=headers,
      json=data
  )


  if response.status_code == 200:
      reply = response.json()["choices"][0]["message"]["content"]

      history.append({
            "role": "assistant",
            "content": reply
        })
      return reply
  else:
      print("Request failed:", response.status_code)
      print(response.text)
      return None

while True:
    message = input("Ask anything: ")

    if message.lower() in  [
    "quit",
    "bye",
    "goodbye",
    "exit",
    "see you",
    "see you later",
    "i'm leaving"
]:
        print("Goodbye!")
        break

    reply = chat(message)

    if reply:
        print("AI:", reply)


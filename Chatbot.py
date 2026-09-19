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


def chat(message):
  data = {
      "model": "openai/gpt-oss-120b:fastest",
      "messages": [
          {
              "role": "user",
              "content": message
          }
      ]
  }

  response = requests.post(
      url,
      headers=headers,
      json=data
  )


  if response.status_code == 200:
      reply = response.json()["choices"][0]["message"]["content"]
      return reply
  else:
      print("Request failed:", response.status_code)
      print(response.text)
      return None

reply = chat("What is Python?")
print(reply)
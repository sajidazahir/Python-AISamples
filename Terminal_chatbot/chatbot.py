import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
)
  
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Explain things clearly for beginners."
    }
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages
    )

print("AI Chatbot started. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot stopped not working.")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

  

    ai_reply = response.choices[0].message.content

    print("AI:", ai_reply)
    print()

    messages.append({
        "role": "assistant",
        "content": ai_reply
    })
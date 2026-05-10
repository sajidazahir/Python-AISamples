# This code demonstrates how to use the Groq API to create a chat completion using the Llama-3.3-70b-versatile model. 

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI coding tutor."
        },
        {
            "role": "user",
            "content": "Write a Python calculator program."
        }

    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
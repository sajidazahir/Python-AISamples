# This code demonstrates how to use the Groq API to  LIST ALL MODELS and then create a chat completion using the Llama-3.3-70b-versatile model.

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Get all available models
models = client.models.list()

print("AVAILABLE MODELS:\n")

# Loop through every model
for model in models.data:

    print("MODEL:", model.id)

    # Ask AI to explain the model
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are an AI expert."
        },
        {
            "role": "user",
            "content": f"Explain what this AI model is best used for: {model.id}"
        }
    ],
        max_tokens=500
    )

print(response.choices[0].message.content)
print("\n-----------------------------------\n")
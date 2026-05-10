# **Simple Chatbot GUI Example (Tkinter, Python):**
# Here's a basic example of a chatbot GUI using Tkinter in Python:

import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
# Put your Groq API key here
client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
)
MODEL = "llama-3.3-70b-versatile"

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Explain clearly for beginners."
    }
]

def send_message():
    user_text = user_input.get()

    if user_text.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_text + "\n\n")
    user_input.delete(0, tk.END)

    messages.append({
        "role": "user",
        "content": user_text
    })

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        ai_reply = response.choices[0].message.content

        chat_box.insert(tk.END, "AI: " + ai_reply + "\n\n")

        messages.append({
            "role": "assistant",
            "content": ai_reply
        })

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI window
window = tk.Tk()
window.title("My Groq AI Chatbot")
window.geometry("700x600")

# Chat display
chat_box = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=80,
    height=30
)
chat_box.pack(padx=10, pady=10)

# Input box
user_input = tk.Entry(window, width=70)
user_input.pack(padx=10, pady=5)

# Send button
send_button = tk.Button(
    window,
    text="Send",
    command=send_message
)
send_button.pack(pady=5)

# Press Enter to send
window.bind("<Return>", lambda event: send_message())

window.mainloop()



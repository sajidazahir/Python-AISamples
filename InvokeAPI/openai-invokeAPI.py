from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)
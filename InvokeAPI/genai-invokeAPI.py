from google import genai

client = genai.Client(api_key="TODO - Get Google AIKey")
response = client.models.generate_content(
    #   model="gemini-2.0-flash",
    # model="gemini-1.5-flash",
    model="gemini-2.0-flash-exp",
    contents="Explain AI agents"
)

print(response.text)
from google import genai

from config import apikey

client = genai.Client(api_key=apikey)  # <-- replace with your real key

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Write a professional resignation email to my boss."
)

print(response.text)


import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=" * 50)
print("🤖 Gemini AI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user
    )

    print("\nGemini:", response.text)
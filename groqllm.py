from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
# secret_key = os.getenv("SECRET_KEY")

# print("API Key:", api_key)

# Set the API key here
client = Groq(api_key=api_key)

# corrected_text="hi helo whatsapp"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant. Text will be provided to you, you need to remove the unnecessary content out of it which doesnt make sense and keep the actual text out of it. Just give the formatted text with perfect format. Nothing else"
        },
        {
            "role": "user",
            "content": corrected_text,
        }
    ],
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_completion_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
)

print(chat_completion.choices[0].message.content)  

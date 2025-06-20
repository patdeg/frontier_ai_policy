from dotenv import load_dotenv
import os
import openai

# Load environment variables from a .env file if present
load_dotenv()

# Create OpenAI client using the API key from the environment
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "tell me a joke?"}],
)

print(response.choices[0].message.content)

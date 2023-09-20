from dotenv import load_dotenv
import os
import requests
import json

# Load .env file
load_dotenv()

# Get API Keyy
api_key = os.getenv("API_KEY")

print(f'My API key is: {api_key}')


# Define the API endpoint and headers

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}


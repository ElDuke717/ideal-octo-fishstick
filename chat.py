from dotenv import load_dotenv
import os
import requests
import json
import time

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("API_KEY")

# Define the API endpoint and headers
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": f'Bearer {api_key}',
    "Content-Type": "application/json"
}

user_prompt = input("What would you like to ask gpt-3.5-turbo?")


def chat_with_gpt():
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "Thanks for helping."},
                     {"role": "user", "content": f'{user_prompt}'}]}

    while True:
        response = requests.post(API_ENDPOINT, headers=HEADERS, json=payload)

        if response.status_code != 200:
            error_data = json.loads(response.text)
            print(
                f"Error: {error_data.get('error', {}).get('message', 'Unknown error')}")
            break

        data = json.loads(response.text)

        # Check if 'choices' exists in the response data
        if 'choices' in data and data['choices']:
            reply = data['choices'][0]['message']['content']
            print(f"ChatGPT's reply: {reply}")
        else:
            print("Unexpected response:", data)
            break

        user_input = input("Your message: ")

        if 'bye' in user_input.lower():
            print("Exiting the chat. Goodbye!")
            break

        payload['messages'].append({"role": "user", "content": user_input})

        # Sleep to prevent rate limiting
        time.sleep(2)


chat_with_gpt()

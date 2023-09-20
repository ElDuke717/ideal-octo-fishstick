from dotenv import load_dotenv
import os
import requests
import json
import time

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

# construct the payload - a list of messages, where each message has a role
def chat_with_gpt():
    payload = {"messages": [{"role": "system", "content": "Thanks for helping."},
                            {"role": "user", "content": "Who is the first president of Antarctica?"}]}


    # sending the API request
    response = requests.post(API_ENDPOINT, headers=HEADERS, json=payload)

    # handling the API response:

    data = json.loads(response.text)
    reply = data['choices'][0]['message']['content']
    print("ChatGPT's reply:", reply)

    # response loop with initial messages for each role - an infinite loop to iteratively process sending the user message and receive responses

    while True:
        response = requests.post(API_ENDPOINT, headers=HEADERS, json=payload)
        data = json.loads(response.text)
        reply = data['choices'][0]['message']['content']
        print("ChatGPT's reply:", reply)

        user_input = input("Your message: ")
        payload['messages'].append({"role": "user", "content": user_input})

        user_input = input("Your message: ")
        if 'bye' in user_input.lower():
            break

        payload['messages'].append({"role": "user", "content": user_input})

        time.sleep(2)  # Rate limiting

chat_with_gpt()
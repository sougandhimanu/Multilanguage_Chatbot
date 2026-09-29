import openai
import json

with open("cred.json", 'r') as json_file:
    credentials = json.load(json_file)

openai.api_base = credentials["api_base"]
openai.api_key = credentials["api_key"]

with open("cred.json", 'r') as json_file:
    credentials = json.load(json_file)

SERPER_API_KEY = credentials["serper_key"]


def get_chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
  
def chat_with_gpt(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        gpt_response = response["choices"][0]["message"]["content"]
        
        unsure_phrases = [
            "I'm not sure", "I don't know", "cannot help", "don't have information",
            "I'm unable to", "As an AI language model", 
            "I am not able", "I recommend checking", "I suggest visiting"
        ]

        dynamic_queries = [
            "ipl schedule", "ipl 2025 schedule", "match schedule", "cricket schedule",
            "live cricket score", "match result", "football match", "yesterday's news", "latest news"
        ]

        if any(phrase.lower() in gpt_response.lower() for phrase in unsure_phrases):
            print("GPT was unsure. Triggering web search for:", user_input)
            web_response = search_web(user_input)
            
            # Return a clean response combining both
            final_response = (
                "I'm unable to provide real-time news updates. "
                "However, here are some web results that might help:\n\n"
                f"{web_response}"
            )
            return final_response

        elif (any(keyword in user_input.lower() for keyword in dynamic_queries)) or \
        (any(phrase.lower() in gpt_response.lower() for phrase in unsure_phrases)):
            print("Triggering web search for:", user_input)
            web_response = search_web(user_input)

            # Final cleaned output
            final_response = (
                "Here is what I found:\n\n"
                f"{web_response}"
            )
            return final_response
        else:
            return gpt_response


    except Exception as e:
        return f"Error: {str(e)}"

import requests


def search_web(query):
    API_KEY = SERPER_API_KEY  # Replace with your API Key
    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "q": query
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        # Extract top 3 results
        if "organic" in result:
            top_results = result["organic"][:3]
            formatted_results = "\n\n".join([f"- {item['title']}\n{item['link']}" for item in top_results])
            return f"Here are some web results:\n\n{formatted_results}"
        else:
            return "No relevant web results found."
    except Exception as e:
        return f"Web search error: {str(e)}"


from dotenv import load_dotenv
from openai import OpenAI
import os

#Load the environment variables
load_dotenv()

#Save api key to variable
api_key = os.getenv('CHATGPT_API_KEY')

#Check to see if API key is empty
if api_key is None:
    raise ValueError("CHATGPT_API_KEY environment variable is not set.")

#Create client object for API retrieval
client = OpenAI(api_key = api_key)

#Function that sends API request and parses JSON response into a useable string to be returned
def chatgpt_response(prompt):
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role': 'user', 'content': prompt}],
        temperature = 1,
        max_tokens = 100
        )
    response_dict = response.get('choices')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict['choices'][0]['message']['content']
        return prompt_response
    
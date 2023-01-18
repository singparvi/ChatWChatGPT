# %%
import openai as ai
# Packages for env or isolating sensitive information to a secret file
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load env variables from .env
# create your own .env file and assign your own API_Key like:
# API_Key = '<insert your API key here from beta.openai.com -> View API keys'

dotenv_path = join('.env')
load_dotenv(dotenv_path)
ai.api_key = os.environ.get("API_Key")

def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=100,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return print(completions.choices[0].text)

generate_gpt3_response("word the following email better: \
Sample: Perfect! I have taken the time to check the public link and it is fixed. Thank you for your prompt action. ")



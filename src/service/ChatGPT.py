from src.config import Config
import openai

"""
A method for working with ChatGPT Api, 
it was made as a class so that the bot could be easily scaled
"""

class GPT():

    def __init__(self, token):
        openai.api_key = token

    #sending text request ( import - en ;  export - en )
    async def SendText(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        return response
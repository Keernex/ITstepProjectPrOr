import os
import openai
from api_token import *

key_keeper = "api_token.py"
parameter = "OPENAI_API_KEY"

def check_api():
    api_key = str(input("Enter your 'OpenAI' API-Key: "))
    with open(key_keeper, "a", encoding="utf8") as config:
        config.write(f"\n{parameter} = '{api_key}'")
        print("TOKEN was added successfully.")

    with open(key_keeper, "r+", encoding="utf8") as config:
        empty_lines = config.readlines()
        config.seek(0)
        config.writelines(line for line in empty_lines if line.strip())
        config.truncate()

def get_answer_from_chat_gpt():
    openai.api_key = eval(parameter)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="",
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    print(response['choices'][0]['text'])

def connect_to_openai():
    if os.path.isfile(key_keeper):
         with open(key_keeper, "r", encoding="utf8") as config:
              content = config.read()
              if parameter not in content:
                  check_api()
              else:
                  exec(content)
                  get_answer_from_chat_gpt()

if __name__ == '__main__':
    connect_to_openai()
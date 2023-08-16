import os
import openai
from api_token import *
import requests
import re
import customtkinter as ctk
from PIL import Image

from chat_gpt import *
from input_api_token import *
from check_key import *

key_keeper = "api_token.py"
parameter = "OPENAI_API_KEY"

def get_answer_from_chat_gpt(master):
    openai.api_key = eval(parameter)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Chat GPt, you check people for professional orientation, your task is to analyze the questions and answers to them, after which you have to make a detailed analysis in Ukrainian.This analysis should include an answer, which profession is more suitable for the user, and pay attention to writing literacy."},
            {"role": "user", "content": master}
        ]
    )
    answer_gpt_chat.configure(state="normal")
    answer_gpt_chat.delete("1.0", "end")
    answer_gpt_chat.insert("1.0", response.choices[0].message.content)
    answer_gpt_chat.configure(state="disabled")

def connect_to_openai(master):
    if os.path.isfile(key_keeper):
         with open(key_keeper, "r", encoding="utf8") as config:
              content = config.read()
              if parameter not in content:
                  check_api()
              else:
                  exec(content)
                  get_answer_from_chat_gpt(master)
                  return 0




















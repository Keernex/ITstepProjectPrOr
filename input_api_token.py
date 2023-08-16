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

def check_api():
    api_key = input_api_key.get()
    if authorize_with_api(api_key):
        with open(key_keeper, "r", encoding="utf8") as config:
            lines = config.readlines()
        cleaned_lines = []
        for line in lines:
            if re.match(r'^\s*#', line):
                cleaned_lines.append(line)
            else:
                cleaned_lines.append('\n')
        with open(key_keeper, "w", encoding="utf8") as config:
            config.writelines(cleaned_lines)

        with open(key_keeper, "a", encoding="utf8") as config:
            config.write(f"\n{parameter} = '{api_key}'")
            
            label_error.configure(state="normal")
            label_error.delete("1.0", "end")
            label_error.insert("1.0", "TOKEN was added successfully.")
            label_error.configure(state="disabled")

        with open(key_keeper, "r+", encoding="utf8") as config:
            empty_lines = config.readlines()
            config.seek(0)
            config.writelines(line for line in empty_lines if line.strip())
            config.truncate()
    else:
        label_error.configure(state="normal")
        label_error.delete("1.0", "end")
        label_error.insert("1.0", "TOKEN invalid.")
        label_error.configure(state="disabled")
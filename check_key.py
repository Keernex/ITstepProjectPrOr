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

def authorize_with_api(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('https://api.openai.com/v1/models', headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False
    


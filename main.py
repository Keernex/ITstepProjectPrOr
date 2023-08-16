import os
import openai
from api_token import *
import requests
import re
import customtkinter as ctk
from PIL import Image


ctk.set_appearance_mode("System")
app = ctk.CTk()
#app.geometry("1100x750")
app.geometry("1300x800")

#variables

i = 0

array_task=["Які мої сильні сторони і таланти? Які навички і здібності я володію найкраще?",
      "Які професійні галузі чи області цікавлять мене? Що мене надихає і викликає інтерес?",
      "Які цінності мені важливі в роботі? Які принципи і мета є для мене особливо значущими?",
      "Які можливості для кар'єрного розвитку є в різних професіях або галузях, які мене цікавлять? Які кроки потрібно зробити, щоб досягти успіху у цих областях?",
      "Які є вимоги та перспективи на ринку праці для різних професій, які мені цікаві? Які ризики і виклики можуть виникнути у зв'язку з обраною професією?", ""]

array_answer = ["", "", "", "", "", ""]
array_counter = 0

#functions
#functions key
key_keeper = "api_token.py"
parameter = "OPENAI_API_KEY"


def authorize_with_api(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('https://api.openai.com/v1/models', headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

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

def print_answer_gpt_chat():
    global array_task
    global array_answer
    master_m = "Chat GPt, you check people for professional orientation, your task is to analyze the questions and answers to them, after which you have to make a detailed analysis in Ukrainian.This analysis should include an answer, which profession is more suitable for the user, and pay attention to writing literacy."
    master = master_m + "(Question 1):" + array_task[0] + "(Answer 1):" + array_answer[0] + "(Question 2):"+ array_task[1] + "(Answer 2):" + array_answer[1] + "(Question 3):" + array_task[2] + "(Answer 3):" + array_answer[2] + "(Question 4):" + array_task[3] + "(Answer 4):" + array_answer[3] + "(Question 5):" + array_task[4] + "(Answer 5):" + array_answer[4]
    print(master)
    connect_to_openai(master)
    return 0

#functions counter
def update_counter():
    counter_test_top.configure(text=f"Task {i}")
    counter_test_bottom.configure(text=f"{i} with 5")
    return 0

def update_task():
    global array_counter
    task.configure(state="normal")
    task.delete("1.0", "end")
    task.insert("1.0", array_task[array_counter])
    task.configure(state="disabled")
    return 0

def update_answer():
    global array_counter
    array_answer[array_counter-1] = answer.get("0.0", "end")
    print(array_answer)
    answer.configure(state="normal")
    answer.delete("0.0", "end")
    answer.insert("0.0", array_answer[array_counter])
    return 0

def counter():
    global i
    global array_counter
    i = i + 1
    if (i > 1 and i <= 5):
        array_counter = i - 1
        update_counter()
        update_task()
        update_answer()
    elif (i == 6):
        array_counter = i - 1
        update_answer()
        button_end.configure(text="Complete the test")
        answer.destroy()
        task.destroy()
        counter_test_top.destroy()
        counter_test_bottom.destroy()
        button_end.destroy()
        print_answer_gpt_chat()
        return 0
    else:
        counter_test_top.place(relx=0.2, rely=0.35, anchor=ctk.CENTER)
        task.place(relx=0.22, rely=0.45, anchor=ctk.CENTER)
        answer.place(relx=0.22, rely=0.71, anchor=ctk.CENTER)
        counter_test_bottom.place(relx=0.05, rely=0.93, anchor=ctk.CENTER)
        button_end.configure(text="Answer the question")




#images
image_chat = ctk.CTkImage(Image.open("images/chat_gpt_im.png"),size=(100,100))
image_top_chat = ctk.CTkLabel(app,text="",width=100,height=100,fg_color=None, image=image_chat)
image_top_chat.place(relx=0.44, rely=0.1, anchor=ctk.CENTER)

image_python = ctk.CTkImage(Image.open("images/python_im.png"),size=(100,100))
image_top_python = ctk.CTkLabel(app,text="",width=100,height=100,fg_color=None, image=image_python)
image_top_python.place(relx=0.56, rely=0.1, anchor=ctk.CENTER)

image_bottom_telegram = ctk.CTkImage(Image.open("images/telegram_im.png"),size=(50,50))
image_bottom_telegram = ctk.CTkLabel(app,text="",width=50,height=50,fg_color=None, image=image_bottom_telegram)
image_bottom_telegram.place(relx=0.95, rely=0.95, anchor=ctk.CENTER)

image_bottom_instagram = ctk.CTkImage(Image.open("images/instagram_im.png"),size=(45,45))
image_bottom_instagram = ctk.CTkLabel(app,text="",width=50,height=50,fg_color=None, image=image_bottom_instagram)
image_bottom_instagram.place(relx=0.9, rely=0.95, anchor=ctk.CENTER)

image_bottom_spotify = ctk.CTkImage(Image.open("images/spotify_im.png"),size=(55,55))
image_bottom_spotify = ctk.CTkLabel(app,text="",width=50,height=50,fg_color=None, image=image_bottom_spotify)
image_bottom_spotify.place(relx=0.85, rely=0.95, anchor=ctk.CENTER)

#name TEST
label_top_name_test = ctk.CTkLabel(app, text="Verification of professional ability",width=100,height=35,corner_radius = 5,text_color_disabled="#00ADB5",font=('Open Sans', 22))
label_top_name_test.place(relx=0.5, rely=0.22, anchor=ctk.CENTER)

#API key
#name api key
label_mid_name_api_key = ctk.CTkLabel(app, text="Enter your API key",width=100,height=35,corner_radius = 5,text_color_disabled="#00ADB5",font=('Open Sans', 18))
label_mid_name_api_key.place(relx=0.07, rely=0.05, anchor=ctk.CENTER)
#input api key
input_api_key = ctk.CTkEntry(app,width=300,height=35,corner_radius = 5,fg_color="#393E46",border_color="#EEEEEE",font=('Open Sans', 18))
input_api_key.place(relx=0.13, rely=0.1, anchor=ctk.CENTER)
#name link
label_mid_name_link_key = ctk.CTkLabel(app, text="Link on API key",width=100,height=35,corner_radius = 5,text_color_disabled="#00ADB5",font=('Open Sans', 18))
label_mid_name_link_key.place(relx=0.06, rely=0.15, anchor=ctk.CENTER)
#link
link_key = ctk.CTkTextbox(app,width=430,height=20,font=('Oswald', 14),border_width = 1,fg_color="#393E46",border_color="#EEEEEE")
link_key.insert("1.0", "https://platform.openai.com/docs/quickstart/build-your-application")
#link_key.configure(state="")
link_key.place(relx=0.18, rely=0.2, anchor=ctk.CENTER)
#button print api key
button_mid_print_api_key = ctk.CTkButton(app, text="Send API key",width=150,height=50,corner_radius = 5,fg_color="#393E46",border_color="#EEEEEE",font=('Open Sans', 22),command=check_api)
button_mid_print_api_key.place(relx=0.08, rely=0.28, anchor=ctk.CENTER)



#TEST
#name count
counter_test_top = ctk.CTkLabel(app, text="Task 1",width=100,corner_radius = 10, fg_color="#393E46",text_color_disabled="#00ADB5",font=('Open Sans', 22))

#tasks
task = ctk.CTkTextbox(app,width=500,height=100,font=('Oswald', 20),border_width = 1,fg_color="#393E46",border_color="#EEEEEE")
task.insert("1.0", array_task[array_counter])
task.configure(state="disabled")

#enters
answer = ctk.CTkTextbox(app,width=500,height=300,font=('Montserrat', 18),border_width = 1,fg_color="#393E46",border_color="#00ADB5")
answer.insert("1.0", array_answer[array_counter])

#counter
counter_test_bottom = ctk.CTkLabel(app, text="1 with 5",width=60,corner_radius = 10, fg_color="#393E46",text_color_disabled="#00ADB5",font=('Open Sans', 12))



#answer gpt chat
name_gpt_chat = ctk.CTkLabel(app, text="Answer from ChatGPT",width=100,height=30,corner_radius = 10, fg_color="#393E46",text_color_disabled="#00ADB5",font=('Open Sans', 18))
name_gpt_chat.place(relx=0.77, rely=0.26, anchor=ctk.CENTER)

answer_gpt_chat = ctk.CTkTextbox(app,width=500,height=360,font=('Oswald', 22),border_width = 1,fg_color="#393E46",border_color="#EEEEEE")
answer_gpt_chat.insert("1.0", "")
answer_gpt_chat.configure(state="disabled")
answer_gpt_chat.place(relx=0.77, rely=0.52, anchor=ctk.CENTER)
#Error
label_error = ctk.CTkTextbox(app,width=350,height=100,font=('Oswald', 18),border_width = 1,fg_color="#393E46",border_color="red")
label_error.insert("1.0", "There will be mistakes")
label_error.configure(state="disabled")
label_error.place(relx=0.715, rely=0.84, anchor=ctk.CENTER)

#end
button_end = ctk.CTkButton(app, text="Go for testing",width=150, height = 50,font=('Open Sans', 20), fg_color="#393E46",command=counter)
button_end.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

app.mainloop()

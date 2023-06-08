import os
import openai
from api_token import *
from tkinter import *
from tkinter import scrolledtext
import requests
import re

ss=Tk()
ss.geometry("1200x1000")
ss.title("Professional Orientation")
#def
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
    api_key = top_input_apitok.get()
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
            mid_print_er['text'] = "TOKEN was added successfully."

        with open(key_keeper, "r+", encoding="utf8") as config:
            empty_lines = config.readlines()
            config.seek(0)
            config.writelines(line for line in empty_lines if line.strip())
            config.truncate()
    else:
        mid_print_er['text'] = 'Токен недійсний'

def get_answer_from_chat_gpt(master):
    openai.api_key = eval(parameter)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=master,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    mid_print_v['text'] = response['choices'][0]['text']

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

def check_task():
    t1=mid_task1.get("1.0", "end")
    t2=mid_task2.get("1.0", "end")
    t3=mid_task3.get("1.0", "end")
    t4=mid_task4.get("1.0", "end")
    t5=mid_task5.get("1.0", "end")
    t=[t1,t2,t3,t4,t5]
    for i in range(len(t)):
        if len(t[i]) < 10:
            mid_print_er['text'] = f"Текст у питанні {i+1} менший за 30 символів напиши більш розгорнуту відповідь."
            return 0
            break
    mid_print_er['text'] = ""
    input_master_m(t)
    return 0

def input_master_m(t):
    global Task
    master_m = "Chat GPt, you check people for professional orientation, your task is to analyze the questions and answers to them, after which you have to make a detailed analysis in Ukrainian.This analysis should include an answer, which profession is more suitable for the user, and pay attention to writing literacy."
    master = master_m + "(Question 1):" + Task[0] + "(Answer 1):" + t[0] + "(Question 2):"+ Task[1] + "(Answer 2):" + t[1] + "(Question 3):" + Task[2] + "(Answer 3):" + t[2] + "(Question 4):" + Task[3] + "(Answer 4):" + t[3] + "(Question 5):" + Task[4] + "(Answer 5):" + t[4]
    connect_to_openai(master)
    return 0
#top
top_name_pr=Label(ss,text="Тест про професійна придатність",font="32")
top_name_pr.place(x=0,y=0)
top_name_sz=Label(ss,text="Засновник тесту Максим Вернадський",font="12")
top_name_sz.place(x=0,y=20)
#api token
top_name_apitok=Label(ss,text="Введіть свій Api-Token",font="32")
top_name_apitok.place(x=400,y=20)
top_input_apitok=Entry(ss,font="18",width=30)
top_input_apitok.place(x=405,y=40)
top_print_apitok=Button(ss,text="Відправити",bg="#fff",font="20",command=check_api)
top_print_apitok.place(x=800,y=40)

#mid left
Task=["Які мої сильні сторони і таланти? Які навички і здібності я володію найкраще?",
      "Які професійні галузі чи області цікавлять мене? Що мене надихає і викликає інтерес?",
      "Які цінності мені важливі в роботі? Які принципи і мета є для мене особливо значущими?",
      "Які можливості для кар'єрного розвитку є в різних професіях або галузях, які мене цікавлять? Які кроки потрібно зробити, щоб досягти успіху у цих областях?",
      "Які є вимоги та перспективи на ринку праці для різних професій, які мені цікаві? Які ризики і виклики можуть виникнути у зв'язку з обраною професією?"]
#task1
mid_name_t1=Label(ss,text=Task[0],font="18",anchor="nw",width=35,height=5,wraplength=315, justify=LEFT)
mid_name_t1.place(x=10,y=80)
mid_task1=scrolledtext.ScrolledText(ss,font="24",width=35,height=5)
mid_task1.place(x=10,y=120)
#task2
mid_name_t2=Label(ss,text=Task[1],font="18",anchor="nw",width=35,height=5,wraplength=315, justify=LEFT)
mid_name_t2.place(x=10,y=220)
mid_task2=scrolledtext.ScrolledText(ss,font="24",width=35,height=5)
mid_task2.place(x=10,y=280)
#task3
mid_name_t3=Label(ss,text=Task[2],font="18",anchor="nw",width=35,height=5,wraplength=315, justify=LEFT)
mid_name_t3.place(x=10,y=380)
mid_task3=scrolledtext.ScrolledText(ss,font="24",width=35,height=5)
mid_task3.place(x=10,y=440)
#task4
mid_name_t4=Label(ss,text=Task[3],font="18",anchor="nw",width=35,height=5,wraplength=315, justify=LEFT)
mid_name_t4.place(x=10,y=540)
mid_task4=scrolledtext.ScrolledText(ss,font="24",width=35,height=5)
mid_task4.place(x=10,y=620)
#task5
mid_name_t5=Label(ss,text=Task[4],font="18",anchor="nw",width=35,height=5,wraplength=315, justify=LEFT)
mid_name_t5.place(x=10,y=720)
mid_task5=scrolledtext.ScrolledText(ss,font="24",width=35,height=5)
mid_task5.place(x=10,y=800)
#mid right
#print(1)
mid_print_v=Label(ss,text="",bg="#fff",anchor="nw",font="18",width=50,height=30,wraplength=430, justify=LEFT)
mid_print_v.place(x=400,y=120)
#error
mid_print_er=Label(ss,text="",bg="#fff",anchor="nw",font="18",width=40,height=5,wraplength=340, justify=LEFT)
mid_print_er.place(x=400,y=700)
#bottom
botton_buttom=Button(ss,text="Відправити",bg="#fff",font="20",command=check_task)
botton_buttom.place(x=850,y=750)

ss.mainloop()

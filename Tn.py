from tkinter import*
from tkinter import scrolledtext

ss=Tk()
ss.geometry("1200x1000")
ss.title("Professional Orientation")
#def
toren = ""
def check_token():
    global toren
    if len(top_input_apitok.get("1.0", "end")) < 10:
        mid_print_er['text'] = "Введіть Апі токен"
        return 0
    else:
        mid_print_er['text'] = ""
        toren = top_input_apitok.get("1.0", "end")
    return 0

def check():
    t1=mid_task1.get("1.0", "end")
    t2=mid_task2.get("1.0", "end")
    t3=mid_task3.get("1.0", "end")
    t4=mid_task4.get("1.0", "end")
    t5=mid_task5.get("1.0", "end")
    t=[t1,t2,t3,t4,t5]
    for i in range(len(t)):
        if len(t[i]) < 30:
            mid_print_er['text'] = f"Текст у питанні {i+1} менший за 30 символів напиши більш розгорнуту відповідь."
            return 0
            break
    if len(top_input_apitok.get("1.0", "end")) < 10:
        mid_print_er['text'] = "Введіть Апі токен"
        return 0
    mid_print_er['text'] = "Зараз все добре."
    return input_master_m(t)

def input_master_m(t):
    global Task
    master_m = "Чат Бот ти перевіряючий людей на професійну орієнтацію твоє завдання проаналізувати питання і відповіді до них і зробити розгорнутий аналіз."
    master = master_m + "Питання 1:" + Task[0] + "Відповідь до 1:" + t[0] + "Питання 2:"+ Task[1] + "Відповідь до 2:" + t[1] + "Питання 3:" + Task[2] + "Відповідь до 3:" + t[2] + "Питання 4:" + Task[3] + "Відповідь до 4:" + t[3] + "Питання 5:" + Task[4] + "Відповідь до 5:" + t[4]
    print(master)
#top
top_name_pr=Label(ss,text="Тест про професійна придатність",font="32")
top_name_pr.place(x=0,y=0)
top_name_sz=Label(ss,text="Засновник тесту Максим Вернадський",font="12")
top_name_sz.place(x=0,y=20)
#api token
top_name_apitok=Label(ss,text="Введіть свій Api-Token",font="32")
top_name_apitok.place(x=350,y=20)
top_input_apitok=scrolledtext.ScrolledText(ss,font="18",width=30,height=1)
top_input_apitok.place(x=355,y=40)
top_print_apitok=Button(ss,text="Відправити",bg="#fff",font="20",command=check_token)
top_print_apitok.place(x=650,y=45)

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
mid_print_v=Label(ss,text="",bg="#fff",anchor="nw",font="18",width=40,height=30,wraplength=340, justify=LEFT)
mid_print_v.place(x=400,y=120)
#error
mid_print_er=Label(ss,text="",bg="#fff",anchor="nw",font="18",width=40,height=5,wraplength=340, justify=LEFT)
mid_print_er.place(x=400,y=700)
#bottom
botton_buttom=Button(ss,text="Відправити",bg="#fff",font="20",command=check)
botton_buttom.place(x=800,y=750)














ss.mainloop()
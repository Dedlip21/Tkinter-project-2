from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter import messagebox
import random

root=Tk()
root.geometry("750x500")
root.title("Игра - Выбери правильную карточку")

def ch_1(): #Начать играть
    btn_start.destroy()
    btn_bg.destroy()
    btn_rules.destroy()
    btn_exit.destroy()


def ch_4(): #Выйти из программы
    root.destroy()


def ch_3(): #Правила игры
    btn_start.destroy()
    btn_bg.destroy()
    btn_rules.destroy()
    btn_exit.destroy()

    textA=Text(root,height=8, width=50)
    textA.configure(font=("Arial", 18 ))
    l = Label(root, text = "Правила")
    l.configure(font =("Arial", 35))
    Rule = """Есть 3 карты. 2 из этих карт красные. Если вытянешь одну из этих карт - ты проиграл. Но из трех карт есть одна выигрышная зеленая карточка. Вытяни эту карточку чтобы победить."""

    btn_nazad1 = Button(root, text = "Назад")

    l.pack()
    textA.pack()
    btn_nazad1.pack()
    textA.insert(END, Rule)



   

btn_start=Button(root,text="Играть",height=3, width=20,font="Arial 15",command=ch_1)
btn_start.place(x=250, y=50)

btn_bg=Button(root,text="Выбери фон",height=3,width=20,font="Arial 15")
btn_bg.place(x=250,y=150)

btn_rules=Button(root,text="Правила",height=3, width=20,font="Arial 15",command=ch_3)
btn_rules.place(x=250,y=250)

btn_exit=Button(root,text="Выход",height=3, width=20,font="Arial 15",command=ch_4)
btn_exit.place(x=250,y=350)




root.mainloop()
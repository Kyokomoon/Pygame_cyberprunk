from tkinter import *
from Cyberprunk import load
root = Tk()
root.geometry('200x200')
mainmenu = Menu(root)
def answer(event):
    global ANSWER, ANSWER_2, hero_type
    ANSWER = e_1.get()
    ANSWER_2 = e_2.get()
    if var.get() == 0:
        hero_type = 'Gr'
    elif var.get() == 1:
        hero_type = 'Ha'
    elif var.get() == 2:
        hero_type = 'Mex'
    l_1.destroy()
    e_1.destroy()
    l_2.destroy()
    e_2.destroy()
    Gr.destroy()
    Ha.destroy()
    Mex.destroy()
    b_1.destroy()
    load(ANSWER, ANSWER_2, hero_type, root)
    exit()
def start(event):
    b1.destroy()
    b2.destroy()
    l_1.pack()
    e_1.pack()
    l_2.pack()
    e_2.pack()
    Gr.pack()
    Ha.pack()
    Mex.pack()
    b_1.pack()
def out(event):
    exit()
var = IntVar()
var.set(0)
Gr = Radiobutton(text='Gr', variable=var, value=0)
Ha = Radiobutton(text='Ha', variable=var, value=1)
Mex = Radiobutton(text='Mex', variable=var, value=2)

root.title("Cyberprunk 3037")


b1 = Button(text="Старт", width=15 , height=5, bg='#aaffff')
b2 = Button(text="Выход",width=15 , height = 2, bg='#aaffff')
b_1 = Button(text="Создать", width = 15, bg='#aaffff')
e_1 = Entry(width = 19)
e_2 = Entry(width = 19)
l_1 = Label(text='Имя героя:', width = 15)
l_2 = Label(text='Фамилия героя', width = 15)
l_1.config(bd=5, bg='#aaffff')
l_2.config(bd=5, bg='#aaffff')
b1.bind('<Button-1>', start)
b2.bind('<Button-1>', out)
b_1.bind('<Button-1>', answer)

b1.pack()
b2.pack()

root.mainloop()

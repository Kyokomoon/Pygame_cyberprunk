from tkinter import *
def run(inventory, hand):
    global inventory_save, hand_save
    a = Tk()
    a.geometry('440x400')
    inventory_save = inventory
    hand_save = hand
    def menu():
        l1.pack()
        f_left.pack(side=LEFT)
        f_right.pack(side=LEFT)
        f_right_right.pack(side=LEFT)
        lbox.pack()
        take.pack()
        l2.pack()
        lbox2.pack()
        for i in inventory:
            lbox.insert(END, i)
        for i in hand:
            lbox2.insert(END, i)
    def to_box2():
        global inventory_save, hand_save
        if len(lbox.curselection()) > 0:
            select=lbox2.get(0)
            lbox.insert(END, lbox2.get(0))
            inventory.append(lbox2.get(0))
            hand.pop(0)
            lbox2.delete(0)
            inventory_save = inventory
            hand_save = hand
            select=list(lbox.curselection())
            for i in select:
                lbox2.insert(END, lbox.get(i))
                hand.append(lbox.get(i))
                lbox.delete(i)
                inventory.pop(i)
            hand_save = hand
            inventory_save = inventory
            a.destroy()
            
    f_left = Frame(a)
    f_right = Frame(a)
    f_right_right = Frame(a)
    a.title("Инвентарь")
    l1 = Label(f_left, text='Инвентарь', width = 25)
    lbox = Listbox(f_left, width= 25, height = 20, selectmode=EXTENDED)
    take = Button(f_right, text="Взять", width=10, height=3)
    l2 = Label(f_right_right, text="Используется", width = 25)
    lbox2 = Listbox(f_right_right, width= 25, height= 20, selectmode=EXTENDED) 
    take.config(command=to_box2)
    menu()
    a.mainloop()
    return inventory_save, hand_save
    



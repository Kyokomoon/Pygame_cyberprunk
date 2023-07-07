from tkinter import *
chek_1 = 0
chek_2 = 0
time_point_s = 0
time_point_i = 0
time_point_p = 0
ch_s = 0
ch_i = 0
ch_p = 0
skil_lern = []
def run_skill(HP, ST, SH, lern_skill, skils_1, need_s, need_i, need_p, sila, intelekt, protect, points, skil_lern):
    global Frame_2,Frame_4, time_point_s, time_point_i, time_point_p,save_info_sil, save_info_int, save_info_prot, save_info_point, skil_lern_1,chek_for_down,chek_for_up
    b = Tk()
    points = points
    time_point_s = 0
    time_point_i = 0
    time_point_p = 0
    b.geometry('440x400')
    var = IntVar()
    var2 = IntVar()
    var.set(-1)
    var2.set(-1)
    skil_lern_1 = skil_lern
    Frame_1 = Frame(b)
    Frame_2 = Frame(b)
    Frame_3 = Frame(b)
    Frame_4 = Frame(b)
    Frame_6 = Frame(b)
    save_info_sil = sila
    save_info_int = intelekt
    save_info_prot = protect
    save_info_point = points
    chek_for_up = 0
    chek_for_down = 0
    
    def statit():
        global Frame_7, Frame_8, plus1, plus2, plus3, minus1, minus2, minus3, sil_l, int_l, pr_l, sila_l, intel_l, protect_l, save
        sil = ("s = " + str(sila))
        ent = ("i = " + str(intelekt))
        pr = ("p = " + str(protect))
        hp = "Hp = " + str(HP)
        st = "St = " + str(ST)
        sh = "Sheld = " + str(SH)
        pt = "Points = " + str(points)
        l_hp = Label(Frame_1, text=hp, width= 10)
        l_st = Label(Frame_1, text=st, width= 10)
        l_sh = Label(Frame_1, text=sh, width= 10)
        l_sil = Label(Frame_3, text=sil, width= 10)
        l_ent = Label(Frame_3, text=ent, width= 10)
        l_pr = Label(Frame_3, text=pr, width= 10)
        l_point = Label(Frame_3, text=pt, width=10)
        
        Frame_1.pack()
        Frame_3.pack()
        Frame_6.pack()
        l_hp.pack(side = LEFT)
        l_st.pack(side = LEFT)
        l_sh.pack(side = LEFT)
        l_sil.pack(side = LEFT)
        l_ent.pack(side = LEFT)
        l_pr.pack(side = LEFT)
        l_point.pack()

    def menu():
        
        global hp, skil_1, skil_2, skil_3, skil_4, chek_2, lern, text, chek_for_down,chek_for_up,Frame_2,Frame_4
        if chek_1 == 1:
            obgect = [Frame_10,Frame_7, Frame_8,Frame_9, plus1, plus2, plus3, minus1, minus2, minus3, sil_l, int_l, pr_l, sila_l, intel_l, protect_l, save]
            for obg in obgect:
                try:
                    obg.pack_forget()
                except:
                    pass
        chek_2 = 1
        if chek_for_up == 0:
            skil_1 = Radiobutton(Frame_2, text=skils_1[0], variable=var, value=0, indicatoron=0, width = 15, bg='#aaffff', command = change)
            skil_2 = Radiobutton(Frame_2, text=skils_1[1], variable=var, value=1, indicatoron=0, width = 15, bg='#aaffff', command = change)
            skil_3 = Radiobutton(Frame_2, text=skils_1[2], variable=var, value=2, indicatoron=0, width = 15, bg='#aaffff', command = change)
            lern = Button(Frame_4, text="Изучить", width=10, bg='#aaffff',command=lernd)
            text = Text(width=40, height=25)
            chek_for_down = 0
            Frame_2.pack()
            Frame_4.pack()
            skil_1.pack(side = TOP)
            skil_2.pack(side = TOP)
            lern.pack(pady = 5)
            skil_3.pack(side = TOP)
            text.pack()
            chek_for_up = 1
        
        
    def change():
        text.delete(1.0, END)
        if var.get() == 0:
            tet = "Нужно " + str(need_s[0]) + " Силы " + str(need_i[0]) + " Интеллекта " + str(need_p[0]) + " Защиты"
        elif var.get() == 1:
            tet = "Нужно " + str(need_s[1]) + " Силы " + str(need_i[1]) + " Интеллекта " + str(need_p[1]) + " Защиты"
        elif var.get() == 2:            
            tet = "Нужно " + str(need_s[2]) + " Силы " + str(need_i[2]) + " Интеллекта " + str(need_p[2]) + " Защиты"
        text.insert(1.0, tet)
  
    
    def lernd():
        global skil_lern_1
        if var.get() == 0 and need_s[0] <= sila and need_i[0]<=intelekt and need_p[0] <= protect and len(skil_lern) == 0:
            skil_lern_1.append(skils_1[0])
            text.delete(1.0, END)
            text.insert(1.0, "Изучено")
        elif var.get() == 1 and need_s[1] <= sila and need_i[1]<=intelekt and need_p[1] <= protect and len(skil_lern) == 1:
            skil_lern_1.append(skils_1[1])
            text.delete(1.0, END)
            text.insert(1.0, "Изучено")
        elif var.get() == 2 and need_s[2] <= sila and need_i[2]<=intelekt and need_p[2] <= protect and len(skil_lern) == 2:
            skil_lern_1.append(skils_1[2])
            text.delete(1.0, END)
            text.insert(1.0, "Изучено")
        else:
            text.delete(1.0, END)
            text.insert(1.0, "Не хватает очков развития или не изучен предыдущий навык")
        




    
    def stats():
        global chek_1, Frame_7, Frame_8,Frame_9,Frame_10, plus1, plus2, plus3, minus1, minus2, minus3, sil_l, int_l, pr_l, sila_l, intel_l, protect_l, save, point,sil_text, prot_text, int_text, save_info_sil, save_info_int, save_info_prot, save_info_point, chek_for_down,chek_for_up,chek_2
        if chek_2 == 1:
            obgect = [skil_1, skil_2, skil_3, text, lern, Frame_2,Frame_4]
            for obg in obgect:
                try:
                    obg.pack_forget()
                except:
                    pass
        point = points 
    
        def plus_1():
            global time_point_s, point, sil_text, ch_s
            if point > 0:
                time_point_s += 1
                point -= 1
                sil_text = sila + time_point_s
                sil_l['text'] = sil_text
                ch_s = 1

        def plus_2():
            global time_point_p, point, prot_text, ch_p
            if point > 0:
                time_point_p += 1
                point -= 1
                prot_text = protect + time_point_p
                pr_l['text'] = prot_text
                ch_p = 1
        def plus_3():
            global time_point_i, point, int_text, ch_i
            ch_i = 1
            if point > 0:
                time_point_i += 1
                point -= 1
                int_text = intelekt + time_point_i
                int_l['text'] = int_text
                ch_i = 1
        def minus(p):
            global time_point_s, point, time_point_p, time_point_i, sil_text, int_text, prot_text
            if  time_point_s > 0 and p == 1:
                time_point_s -= 1
                point += 1
                sil_text = sila + time_point_s
                sil_l['text']= sil_text
            elif time_point_i  > 0 and p == 2:
                time_point_i -= 1
                point += 1
                int_text = intelekt + time_point_i
                int_l['text']= int_text
            elif time_point_p > 0 and p == 3:
                time_point_p -= 1
                point += 1
                prot_text = protect + time_point_p
                pr_l['text']= prot_text
        def save():
            global sil_text, int_text, prot_text, save_info_sil,save_info_int,save_inf, save_info_prot, save_info_point, ch_s, ch_p, ch_i
            if ch_s == 1 and ch_i ==1 and ch_p == 0:
                prot_text = protect
            elif ch_s == 1 and ch_p ==1 and ch_i == 0:
                int_text = intelekt
            elif ch_i == 1 and ch_p ==1 and ch_s == 0:
                sil_text = sila

            elif ch_s == 1 and ch_i == 0 and ch_p == 0:
                int_text = intelekt
                prot_text = protect
            elif ch_p == 1 and ch_i == 0 and ch_s:
                sil_text = sila
                int_text = intelekt
            elif ch_i == 1 and ch_s == 0 and ch_p:
                sil = int(sil_text)
                prot_text = protect

            ppoint = int(point)
            sil = int(sil_text)
            intt = int(int_text)
            prot = int(prot_text)
            save_info_sil = sil
            save_info_int = intt
            save_info_prot = prot
            save_info_point = ppoint
            b.destroy()
        
        chek_1 = 1
        if chek_for_down == 0:
            chek_2 = 0
            Frame_7 = Frame(b)
            Frame_8 = Frame(b)
            Frame_9 = Frame(b)
            Frame_10 = Frame(b)
            plus1 = Button(Frame_10,text="+",width=2, bg='#aaffff',command = plus_1)
            minus1 = Button(Frame_10,text="-",width=2, bg='#aaffff',command = lambda: minus(1))
            plus2 = Button(Frame_7, text="+",width=2, bg='#aaffff',command = plus_3)
            minus2 = Button(Frame_7, text="-",width=2, bg='#aaffff',command = lambda: minus(2))
            plus3 = Button(Frame_8, text="+",width=2, bg='#aaffff',command = plus_2)
            minus3 = Button(Frame_8, text="-",width=2, bg='#aaffff',command = lambda: minus(3))
            sil_l = Label(Frame_10, text=sila,width=15)
            int_l = Label(Frame_7, text=intelekt,width=15)
            pr_l = Label(Frame_8, text=protect,width=15)
            sila_l = Label(Frame_10,text="Сила")
            intel_l = Label(Frame_7,text="Интелект")
            protect_l= Label(Frame_8,text="Защита")
            save = Button(Frame_9,text="Сохранить", width=10, bg='#aaffff', command = save)
            chek_for_up = 0
            Frame_10.pack()
            Frame_7.pack()
            Frame_8.pack()
            Frame_9.pack()
            sila_l.pack(side=TOP)
            minus1.pack(side=LEFT)
            sil_l.pack(side=LEFT)
            plus1.pack(side=LEFT)
            intel_l.pack(side=TOP)
            minus2.pack(side=LEFT)
            int_l.pack(side=LEFT)
            plus2.pack(side=LEFT)
            protect_l.pack(side=TOP)
            minus3.pack(side=LEFT)
            pr_l.pack(side=LEFT)
            plus3.pack(side=LEFT)
            save.pack()
            chek_for_down = 1

        

   
        
        
    statit()
    skil =Radiobutton(Frame_6, text = "Скиллы",width=10, variable=var2, value=0,indicatoron=0, bg='#EE82EE',command = menu)
    stat =Radiobutton(Frame_6, text = "Стата",width=10, variable=var2, value=1,indicatoron=0, bg='#EE82EE',command = stats)
    b.title("Умения")
    l = Label(width = 20, height = 40)
    
    skil.pack()
    stat.pack()

    b.mainloop()
    return save_info_sil, save_info_int, save_info_prot, save_info_point, skil_lern_1

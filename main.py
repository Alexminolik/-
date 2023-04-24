from tkinter import *


name = input("Введите своё имя: ")
cot = input("Сколько вам лет: ")
gorot = input("Где вы живёти: ")
love = input("Чего ты любишь больше всего: ")
bute = input("Кем ты хочешь быть: ")
podarok = input("Чего хочешь: ")
nic = input("С любовью кто ты 'P.S за места кто ты должно быть твоё имя и на пиши С любовью': ")


root = Tk()
root.geometry("800x700")

lab_Pismo = Label(font="Times 25", text="Письмо Дедушке Морозу", fg="red")
zdraw_lab = Label(font="Times 20", text="Здравствуй, дорогой дедушка мороз!")
name_lab = Label(font="Times 20", text=f"Меня зовут {name}. Мне {cot} лет.")
gorat_lab = Label(font="Times 20", text=f"Я живу в {gorot}.")
Bolche_lab = Label(font="Times 20", text=f"Больше всего я люблю {love}.")
Pomogat_lab = Label(font="Times 20", text=f"Ешё я стараюсь помогать маме с папой и быть {bute}.")
prig_lab = Label(font="Times 20", text=f"Дедушка Мороз, приглашаю тебя и твою внучку")
prig_lab2 = Label(font="Times 20", text=f"Снегурочку в гости на Новый год.")
Pod_lab = Label(font="Times 20", text=f"Привези мне, пожалуйста, в подарок {podarok}")
s_lab = Label(font="Times 20", text=f"Очень надеюсь скоро увидеть тебя.")
s2_lab = Label(font="Times 20", text=f"{nic}")



lab_Pismo.pack()
zdraw_lab.place(x=45, y=50)
name_lab.place(x=45, y=80)
gorat_lab.place(x=45, y=110)
Bolche_lab.place(x=45, y=140)
Pomogat_lab.place(x=45, y=170)
prig_lab.place(x=45, y=200)
prig_lab2.place(x=45, y=230)
Pod_lab.place(x=45, y=260)
s_lab.place(x=45, y=290)
s2_lab.place(x=45, y=320)

root.mainloop()
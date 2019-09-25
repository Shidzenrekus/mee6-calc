#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################
# Вычисление итогового опыта и числа сообщений до уровня n   #
# GNU GENERAL PUBLIC LICENSE VERSION 3.0		             #
# https://www.gnu.org/licenses/gpl.html                      #
# by Denis Shestyora aka Shidzenrekus                        #
##############################################################
 
from tkinter import *

root = Tk()
root.title("Калькулятор опыта Mee6")
root.geometry("360x280")

def calc():
    global mes_count
    global exp
    exp = [0,0]
    for i in range(n.get()):
        exp[0] = 5*(n.get()**2)+50*n.get()+100
        exp[1] += exp[0]

    exp[0] = StringVar(value=exp[0])

    if mes.get() == 1:
        mes_count = exp[1]/20
        mes_count = StringVar(value=mes_count)

    show_message()

def show_message():
    message_label1.config(text="Опыт до следующего уровня: {}".format(exp[0].get()), justify=LEFT)
    message_label1.place(relx=.5, rely=.3, anchor="c")
    if mes.get() == 1:
        message_label2.config(text="Сообщений: {}".format(mes_count.get()), justify=LEFT)
        message_label2.place(relx=.5, rely=.35, anchor="c")
    else:
        message_label2.place_forget()
 
n = IntVar()
mes = IntVar()

message_label1 = Label(root)
message_label2 = Label(root)

message_entry_label = Label(text="Введите требуемый уровень").place(relx=.5, rely=.1, anchor="c")

message_entry = Entry(textvariable=n).place(relx=.5, rely=.2, anchor="c")
 
message_button = Button(text="Посчитать", command=calc).place(relx=.5, rely=.5, anchor="c")

message_count = Checkbutton(text="Среднее кол-во сообщений до уровня?", variable=mes,onvalue=1,offvalue=0).place(relx=.5, rely=.7, anchor="c")

root.mainloop()

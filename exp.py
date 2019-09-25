#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################
# Вычисление итогового опыта и числа сообщений до уровня n   #
# GNU GENERAL PUBLIC LICENSE VERSION 3.0		             #
# https://www.gnu.org/licenses/gpl.html                      #
# by Denis Shestyora aka Shidzenrekus                        #
##############################################################

import sys
sys.argv.remove(sys.argv[0])

if len(sys.argv) < 1 or sys.argv[0] == "--help":
	exit("Синтаксис командной строки: python exp.py n [-m]\nn — уровень, итоговый опыт которого вы хотите вычислить.\n-m — аргумент, показывающий среднее арифметическое число сообщений, которые вам необходимо отправить для получения уровня n.")

if len(sys.argv) > 1 and sys.argv[1] == "[-m]":
	exit("Вводите -m без квадратных скобок. :)")

n = int(sys.argv[0])
exp = [0,0]
for i in range(n):
	exp[0] = 5*(n**2)+50*n+100
	exp[1] += exp[0]

print ("{}".format(exp[0]))

if len(sys.argv) > 1 and sys.argv[1] == '-m':
        mes = exp[1]/20
        print ("{}".format(mes))

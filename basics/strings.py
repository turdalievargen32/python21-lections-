"==========strings========="
# строки=  неизменяемый тип данных который предназначен для хранения текста(последовательности символов ) зключенного в одинарные или двойные кавычки 
# Синтаксис - 

from os import sep
from tkinter import CENTER
from turtle import title


string1 = 'строка одинарными кавычкасм'
string2 = "строка  двойными кавычками "
#error = 'не правильная строка "
string3 = "don't" # внутри двойных кавычек все однинарные - просто символы 
string4 = '"Makers bootcapm"' # внутри одинарных кавычек все двойные - просто символы 


string5 = '''  
Многострочный текст
в тройных кавычках 

'''
string6 = """ 
Многострочный текст
в двойных кавычках 
Тут можно ставить любые кавычки 'any' or "hey"

"""

"=========================Экранизация строк===================="
 # экранизация спец- симвалов 
"\n" # перенос на новую строку 
'\t' # табуляция  
'\\' # отображение \ (потому что он является инструкцией, которая влияет на ваш код )
'\'' # shows ' 
"\'" # shows "
'\r' # вохвращение каретки в начало
'\v' # пе ренос на новую строку со смещением вправо н длину предыщущей строки 
 
'hello\nworld' 
# hello       world 
'чтобы эранировать нужен символ \\'
# чтобы эранировать нужен символ \ 

'My website is Latracal \rSolution'
# Solutionte is Latracal 

'hello\vworld'
# hello 
#       world 


"=============Форматирование строк================"
title = 'Плов'
price = 1300
format1 = f'Название: {title}, Цена: {price}'
# Название: Плов, Цена: 1300

format2 = 'Название: %s, Цена: %s'
print(format2 % ("Гуляш", "250"))
print(format2 % ("Самсы", "70"))
# Название: Гуляш, Цена: 250
# Название: Самсы, Цена: 70

format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35

"================methods of strings=============="
# методы типов дынных - фунуции к которым мы обращаемся через точку 
dir(str) # check all methods of classes(type of date)

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase() # 'hELLO'
'hello world'.title() # 'Hello World'
'hello world'.capitalize() # 'Hello world'
'hello'.center(11) #'    hello     '
'hello'.count('l') #2 
'hello'.count('ll') #1
'hello hello'.count('hello') #2 
'hello'.count('w') #o
'hello world'.startswith('hell') # True 
'hello world'.startswith('ld') # False
'hello world'.endswith('ld') #True

'hello world'.find(' ') # 5 
'hello world'.find('o') # 4
'hello world'.rfind('o') #7
'hello world'.find('wo')# 6 

'hello world'.split() # ['hello world']
'hello world'.split('0') ['hell', ' w','rld']
'$'.join(['hello','world']) # 'hello$world'
' '.join(['hello','world']) # 'hello world'
''.join(['hello','world']) #'helloworld
'o'.join('hello world'.split('o')) # 'hello world'

# конкатесация - склеивание строк 


"===========Индексы=============="
# индексы - порядковый номер символа в строке 
'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] #'h'
string[6] #'w'
string[5] #' '

# срез - подстрока строки 
string[0:6] # 'hello '
string[2,4] # 'll'
string[0:5][2:4] # 'll'
string[:] # 'hello world 
string[::3] # 'hlwl'
string[::-2] # 'drwolh






"==============доп.инормация============="
a = 4 
print(hash(a))  # 4 



 









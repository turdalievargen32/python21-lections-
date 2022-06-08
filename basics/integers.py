# heloo 
"=============переменные========"
# переменные - это ссылки на ячейки памяти, где хранятся какие-то данные  

#a = 4
#b = 4  
#a + b 
#print(id(a)) 
#print(id(b)) 
"==================Ввод и вывод данных=========="
# print - функция вывода данных в терминал
# input - функция ввода данных с терминала 
b = input()
print("any mumber",  b,)
 
"==============Числа=========="
b = 10.2 
# int(intrgers) - целые цисла (5,7,766,56,34,0)
# float - вещественные(с плаващей точкой) (0.4 , 54.05, 0.443)
# decimal - точное вещественное число 
# чтобы использовать Decimal нужно его импортировать 
from cmath import sqrt
from decimal import Decimal
c= Decimal(0.1)

# complex - комплексные цисла 
#complex(1, 5)

"======================ОПЕРАЦИИ НАД ЦИСЛАМИ=================="
5 + 5 # plus 
5 - 4 # minus 
2 * 4 # multiplication
15 / 3 # division with float(5.0)
15 // 2 # division ( int 5)
5 % 2 # the remaider of division
5 ** 3 # exponentation(возведение в степень)
25 ** 0.5 # square root 
#sqrt -function for finding square the integers
# for working we need to import her from library of math 
from math import sqrt 
sqrt(25) #5
sqrt(36) #6

# модуль числа - из отрицательного цисла сделать положительное |-5|= 5
abs(-5) # 5 

pow
#1 - функция число возводит в опредкленную степень
#2 - возвращает остаток отделения результата 1 действия на третье число 

pow(2,3) # 8 = 2**3
pow(2,3,4) # 8 % 4 = 0 

#divmod - function which get 2 numbers and back 2 numbers, 
# where the first is full part of division, the second is reamider of division
#divimod(15,2 ) # 7,1 

# round - finction which the rounds number 
round(5.6) # 6 
round(4.5) # 5 
round(3.1) # 3 
round(7.49) #7 (it takes the first number after dot)
# we can indicate how many the number of integers stay after comma 
round(10.0475, 3) # 10.048 
round(10.0474, 3) # 10.047

 









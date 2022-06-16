'==========================Comprehensions============================'
# comprehensions - генерация последовательностей в одну строку используя цикл 

# 1 результат for элемент  in итерируемый объект 
# 2 ркзультат for элемент  in итерируемый объект [if фильтр]



'мы должны создать список состоящих из цисел от 1 до 10'
from __future__ import print_function


list_ = []
for i in range(1,11):
    list_.append(i)
# list = [1,2,3,4,5,6,7,8,9,10]

list_ = list((i for i in range(1,11)))
# list_ = [1,2,3,4,5,6,7,8,9,10]


list_ = [(i*2 for i in range(1,11))]

"=============================list.comprihensions================================================"

'мы должыны созать список из четных цисел от 1 до 10'
list_ = []
for i in range(1,11):
    if not i % 2:
        list.append()

list_ = [i for i in range(1,11) if not i %2 ]

list_ = [i for i in range(2,11,2)]
# list_ = [2,4,6,8,10]

list_ = [print(i) for i in range(10)]
#None

list_ = ['hello' for i in range(10)]
# ['hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello']

print([input() for i in range(10)])
# будет спрашивать на каждой итерации 

'создать списрк от 1 до 10, но вместо цифр написать четное или не четное '

list_ = [(i,'нечетное' if i % 2 else 'четное') for i in range(1,11)]    # мы использовали тернарный оператор 
print(list_)
 

# созать список из цисел находяхихся в  list_ заменив их на четное или нечетное 

list1 = [1,'hello', 3,'world',3,5,7,8]

list_=['нечетное' if i % 2 else 'четное' for i in list1 if type(i)==int]
print(list_)


'=================================Dict comprehensions=================================== '
#  создать словать гду ключи - числа от 1 до 10  а значение эти числа в иде строки

 dict__ = dict((i,str(i)) for i in range(1,11))





 "даны 2 списка создайтк словарь где ключи - элементы 1 списка а значения - второго"

list3 = [1,2,3,4,5]
list4 = ['a','b','c','d','e']
dict_ = dict( (list3[index],list4[index]) for index in range(len(list3)) )
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


list3 = [1,2,3,4,5]
list4 = ['a','b','c','d','e']
dict_ =  { (list3[index],list4[index]) for index in range(len(list3)) }
# {(3, 'c'), (5, 'e'), (4, 'd'), (1, 'a'), (2, 'b')}

'создайте копию словаря'
dict4 = {"a";1,"b":2,"c":3}
dict_5 = {key:value for key,value in dict3.items() }
#{"a";1,"b":2,"c":3}
 

'поменяйте ключ и значение местами'
dict1 =  {"a";1,"b":2,"c":3}
dict2 = {value : key for key,value in dict1.items()}
# {"1";a,"2":b,"3":c}

dict1 = {
"a" : [1,2,3,4,5],
"b" : [10,232,23,],
'c':[23,45,56],
'd':[4,6,4]

}
dict2 = {key:sum(value) for key,value in dict1.items() }
print(dict2)
#{'a': 15, 'b': 265, 'c': 124, 'd': 14}

'===================================вложенные comprehensions========================================'
'создайте словарь где ключами бцдут числа от 1 до 10 а значениями списки от 1 до числа-ключа'

dict_ = { i:list(range(1,i+1))for i in range(1,6)}


dict_ = { i:[j for j in range(1,i+1)] for i in range(1,6)}
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

"создайте список состоящий из 10 списков в которых строка  'hello world  повторяется 5 раз "
list_ = [
    ["hello world" for i in range(5)]
    for i in range(10)
]
# [['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world']]

list_ = [
    [i for i in range(5)]
    for i in range(10)
]
# [[0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4]]
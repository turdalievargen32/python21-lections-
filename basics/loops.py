"============================Циклы==============================="
# циклы это блок кода кот орорый повторяется несеольео раз 
# while 
# for - это цикл который работает с итерируемыми объуктами. цикл заканчивает свою работу когда он дошел до конца 
# while - цикл который работает до тех пор пока условие верное 

count = 10
while count !=0:
    print(count)
print('end')
# 10,9,8,7,6,5,4,,3,2,1 end

a = 0
while a:
    print('hello')

# вообще не сработает 


for i in [1,2,3]:
    print(i)
# 1 2 3

for i in range(5):
    print(i)
# 0,1,2,3,4

for i in range(1,5):
    print(i)
# 1,2,3,4

num = 12345678
sum = 0 
for i in str(num):
    sum = sum + int(i)
print(sum)


for i in []:
    print(i)


string = 'hello'
for i in string:
    print(i)
    string = string + 'hello'
    print(string)
# отработает тоько 5 раз так как у переменной string ссылка на 46 строке менялась а у цикла 44стр нет 


"========================ключевые слова в циклах=========================================="
#break - полностью выйти из цикла
#continue - перейти  к следующей итерации 

for i in range(10):
    if i == 3:
        print(i)
        break

for i in range(10):
    print(i)
    if i == 3:
        break


for i in range(10):
    print(i)
    if i == 3:
        continue


for i in range(10):
    print(i)
    for j in range(10):
        print(j)
        if j==5:
            break
    if i == 2:
        break

list_ = [2,2,2,4,1,5,5,6,6,7,2,4,5,8,2]
while 2 in list_:
    list_.remove(2)
    print(list_)


list_ = [2,2,2,4,1,5,5,6,6,7,2,4,5,8,2]
while 2 in list_:
    list_.remove(2)
print(list_)

'=========================итерирование словарей========================================='

dict1 ={"a":1,"b":2,"c":3,"d":4}
# при итерации словаря мы мудем получать его ключи
for key in dict1:
    print(key)
# "a","b","c","d"

for key in dict1.keys():
    print(key)
# "a" "b" "c" "d"

# при итерации  dict_values, мы будем получтаь значения славаря
for value in dict1.values():
    print(value)
# 1 2 3

for key in dict1:
    print(dict1[key])
    # также вывыедем его ключи 

# при итерации dict_items мы будем получать tuple из ключа и значения 
for items in dict1.items:
    key = items(0)
    value = items(1)
    print(key, value)

#  мы можем распокаовать tuple на 2 переменные
for key,value in dict1.items():
    print(key,value)

# for key, value in dict1.keys():
# # ValueError: not enough values to unpack(expected 2 , got 1)
#  так как метод keys возвращает нам только 1 элемент а мы распаковываем его на 2 переменные 

for a,b,c in [ (1,2,3), (4,5,6),(7,8,9)]:
    print(a,b,c)
# a=1 b=2 c=3 (iter1)
# a=4 b=5 c=6 (iter2)
# a=7 b=8 c=9 (iter3)


for a,b in [ (1,2), (3,4),(5,6)]:
    print(a,b,)
# a=1 b=2  (iter1)
# a=3 b=4  (iter2)
# a=5 b=6  (iter3)


a = []
for i in a:
    print('for')
else:
    print("else")
# сработает если только цикл вообще не сработает



a = 1
while a :
    print("while")
    if a ==1:
        break
else:
    print("else")
# else сработает если цикл был прерван break 

'======================================Функциии==============================================================='
# функции - именинованный блок кода который может принимать аргументы и возвращать результат 


def my_sum(a,b):
    return a/b, a+b, a*b  
    

res = my_sum(5,4)
print(res)

'=====================================Пареметры=========================================='
# параметры это локальные переменнные внутри функции, значения которых мы задаем при вызове функции (переменнные которые мы указали внутри скобок при создании фукции(когда написали def))
# сначала определяем обязательные потом с дефолтом потом *,  в конце **

'=================Виды параметров=================='
# 1) обязательные
# 2) необязательные
# 2.1) по деволту (по умолчанию) которое мы передаем через =
# 2.2) args
# 2.3) kwargs 
'''
args - tuple , в который нам приходят все аргументы которые были переланы через запятую(кроме обязательных и по дефолту )

kwargs - dict, в который нам приходят все аргументы которые были преданы ввиде ключ=значение(кроме именованных)
'''

# 2.3) kwargs
 
'======================================Аргументы==========================================='
# аргументы значения которые мы передаем параметрам при вызове функции

'===============================Виды аргументов=================================='
# 1) позиционные - 
# 2) именованные (ключ=значение)

def sum_or_10(a,b=10):
    # b - параметр с дефолтом
    return a + b  
print(sum_or_10(2,3))
print(sum_or_10(1))
print(sum_or_10(2,9))
print(sum_or_10(15))


def func(*args, **kwargs ):
    print(args,kwargs)
func(1,2,4,5,6,8,9,4,56,76,5), {'a':5} (c=3, b=2)

def func2(a,b=5, *c, **d):
    print('a-', a)
    print('b-', b)
    print('c-',c)
    print('d-',d)

# func() - TypeError: func2 missing 1 requared 

'====================*=========================='
# * - знак умножения, еще распаковка 

list_ = [1,2,3,4,5]
list2 = [*list_] # распаковываем значения в списке в новый список 

dict_ = {'a':1,'b':2}
dict2 = {**dict_} # распаковываем пары в словаре в новый словарь 
print(dict2)


def aigerim():
    print("Несу маркер")
    return "marker"

def nastya():
    print("Айгерим, принеси пожалуйста маркер")
    marker = aigerim()
    print("Айгерим принесла", marker)

nastya()


len( [1,2,3] ) # 3

def my_len(obj):
    count = 0
    for i in obj:
        count = count + 1
    return count

print(my_len([1,2,3,4,5])) # 5
print(my_len('sdfghjkl')) # 8



database = {
    "Бекзат": "скала",
    "Эртай": "пароль",
    "Оомат": "Кыргызстан",
    "Имран": "12345",
    "Жийде": "return",
    "Манас": "Маке",
    "Арафат": "54321",
    "Элжаз": "парол",
    "Гулсана": "312",
    "Эркайым": "Айдин",
    "Бекназ": "Арёль",
    "Эдиль": "ьлорап",
    "Айгул": "май",
    "Закир": "@@@",
    "Бегайым": "makers",
    "Мырзайым": "Bootcamp2221",
    "Даниэл": "covid19",
    "Жибек": "1404",
    "Айгерим":"moon02",
    "Калысбек": "стол",
    "Ырыс": "suuuuuuuuiiiiiiiiiiii",
    "Айканыш": "qwerty",
    "Арген": "11172332",
    "Нурмухамед": "Не верный",
    "Бектур": "0101",
    "Алан": "душу питона",
    "Жаангер": "ох блин",
    "Богдан": "Кудайберген",
    "Айгерим": "синий маркер",
    "Настя": "Python21"
}

def login(username):
    for i in range(3):
        if username in database:
            password = input("Введите пароль: ")
            if password == database[username]:
                print("Success")
                break
            else:
                print("Incorrect password")
        else:
            print("Incorrect username")
            break

login(username="Мырзайым")


def translate(string):
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"    
    if string[0] in eng:
        dictionary = str.maketrans(eng, ru)
    else:
        dictionary = str.maketrans(ru, eng)
    return string.translate(dictionary)

print(translate(input("Введите слово: ")))


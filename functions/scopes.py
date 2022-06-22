'========================Области видимости и пространства имен===================='
locals() # - возвращает словарь со всеми локальными переменными
globals() # - возвращает словарь со всеми глобальными  переменными 

#LEGB = local,enclosed,global,build-in

# Build-in - встроенные простраства имен (все встроенные переменные(print,input,max,min,len,abs,int,str,dict...))


# globals() - глобальное пространства имен( все переменные внутри файла, которые создали мы )
# чтобы узнать что находиться в глобальном пространстве можно использовать функцию globals

'Enclosed' # это пространство кторое находиться между двумя пространствами 

'Local' - # 'какое -то закрытое пространство'

def func():
    #enclosed простравнство 
    a = 'func'
    def inner_func():
        a - 'inner func'    
    # local пространство    
    inner_func()
    print(locals())

print(locals())
print(globals())



эртай = 'алиби'

def func():
    nastya = 'python21'
    print(эртай) # алиби

# func()
# print(nastya)   - NameError: name 'nastya' is not defined


count = 0

def add():
    print(count)
    count += 1 # UnboundLocalError: local variable 'count' referenced before assignment

def add():
    global count # доступ на изменение глобальной переменной count
    count += 1
    print(count)

add()
add()
add()
print(count)
# 1 2 3 3


a = 'global'

def outer_func():
    a = 'enclosed'

    def inner_func():
        a = 'local'
        print(a) # local

    print(a) # enclosed
    inner_func()

print(a) # global
outer_func()

# global enclosed local


def count(i):
    counter = 0

    def add():
        nonlocal counter # доступ на чтение и изменение локальной переменной counter 
        print(counter)
        counter += 1

    for _ in range(i):
        add()

count(10)
# 0 1 2 3 4 5 6 7 8 9

def func():
    a = '1'
    def inner_func():
        def inner2_func():
            nonlocal a # доступ на чтение и изменение локальной переменной a
            a = 2
        inner2_func()
    inner_func()
    print(a)
func() # 2
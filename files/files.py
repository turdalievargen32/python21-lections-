"==========================Раблта с файлами================================"
# open - фуекция которая открывает файл
"==================Режими======================"
# r  - read(только для чтения)
# w = write (только для записи(сначала все из файла удаляется, а потом записывается))
# a - append (дозапись(все новое добавляется в конец))
# x - создает файл если он уже существует - ошибка
# rb - чтение в бинарном виде 
# wb - запись в бинарном виде 
# ab - дозапись в бинарном виде


# open("test.txt") FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
"когда мы не указываем режим - по умолчанию чтение"


"Когда мы открываем файл в рижиме w- он создает пустой файл и потом туда записывает данные "
# open('test.txt', 'w') -  создает пустой файл 



"Когда файла нет - он создает его"
# open('test.txt', 'a')

'============================READ=================================='
file = open('test.txt') # открываем новый файл 
res = file.read() # считывает весь файл и возвращает в строку
print(file.read(5)) # пустая строка, так как каретка находится в самом конце файла
file.seek(0) # каретка переходит в индекс 0 (в начало файла)
print(file.read(5)) # 'hello' (считал 5 символов)
print(file.read(5))  # ' worl' (считал следующие символы)
print(file.tell()) #10 (показывает текущее положение коретки)
res = file.readlines()
print(res)
file.close() # обязательно закрываем 



'==============================WRITE==============================='
file = open("test.txt", 'w') # открывает файл, почистил
res = file.read()
print(res)
# метод read нельзя использовать при режиме записи и дозаписи (c w+ сработает)

file.write('hello world\n') # в файл записали строку 'hello world'
file.write('Makers Bootcamp\n') # после этого дописывает "makers bootcamp"

file.writelines(['line1\n', 'line2\n', 'line3\n'])
# проинимает список со строками и дозаписывает их в файл
file.close() # обязательно закрываем файл 



"=================With========================"
# with - это конструкция которая в начале констукции вызывает метод __enter__, а в конце вызывает __exit__

class Test:
    def __enter__(self):
        print("Начало работы")
        return self
    
    def __exit__(self, *args, **kwargs):
        print("Конец работы")
    
    def hello(self):
        print("Hello world")

with Test() as test:
    test.hello()

# Начало работы
# Hello world
# Конец работы


file1 = open('test.txt', 'w')
file1.write('hello')
file1.close()
file2 = open('test.txt', 'w')
file2.write('world')
file2.close()

file = open("test.txt", 'w+')
file.write("Hello world\nMakers\nBootcamp")
file.seek(0)
res = file.read()
file.seek(0)
file.write("New lines\n")
file.write(res)
file.close()



with open('test.txt') as file:
    print(file.read())
    print(file.closed()) #False
print(file.closed) # True

string = 123456789
print(int("".join(map(lambda x: x+x, list(str(string))))))
#112233445566778899




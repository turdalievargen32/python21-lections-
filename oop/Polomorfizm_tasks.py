#1
a = '12342342345' 
b = [1,['a',5,6],2,3,4,5] 
c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 

list_ = []
list_.append(a)
list_.append(b)
list_.append(c)

for x in list_:
    print(len(x))


#2
class Dog():
    def voice(self):
        print('Гав')


class Cat():
    def voice(self):
        print('Мяу')

barsik = Cat()
rex = Dog()

def to_pet(animal):
    animal.voice()

print(to_pet(barsik))
print(to_pet(rex))

# 3
class Person():
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}'


class Employee(Person):
    def __init__(self,name,last_name,work,status):
        super().__init__(name,last_name)
        self.work = work
        self.status = status
    
    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'

class Student(Person):
    def __init__(self, name, last_name, university,course):
        super().__init__(name,last_name)
        self.university = university
        self.course = course
    
    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'

person = Person('Иван', 'Петров')
employee = Employee('Иван', 'Петров', 'Рога и копыта', 'директор')
student = Student('Иван', 'Петров' 'КГТУ', 3, 'sks')

def get_human_info(obj):
    print(obj.get_info())

get_human_info(employee)
get_human_info(student)
get_human_info(person)


# 5
class OS():
    def __init__(self,version):
        self.version = version

class Windows(OS):
    def copy(self, text):
        self.text = text
        return f'скопирован текст "{self.text}" горячими клавишами CTRL + C'

class MacOS(OS):
    def copy(self, text):
        self.text = text
        return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'

class Linux(OS):
    def copy(self,text):
        self.text = text 
        return f'скопирован текст "{self.text}" горячими клавишами CTRL + SHIFT + C'

win = Windows(11)
mac = MacOS(10)
lin = Linux(2)

print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))



# 7 
class Money():
    def __init__(self,country,symbol):
        self.country = country
        self.symbol = symbol

class Dollar(Money):
    rate = 84.80 
    
    def exchange(self,amount):
        res =  self.rate * amount
        return f'$ {amount} равен {res} сомам'

class Euro(Money):
    rate = 98.40
    
    def exchange(self,amount):
        res = self.rate * amount
        return f'€ {amount} равен {res} сомам'


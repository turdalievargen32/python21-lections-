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

# 4 
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 1 / 2 * self.base * self.height

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length**2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2

triangle = Triangle(6, 3)
square = Square(4)
circle = Circle(5)

print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area())


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

# 6
class Language:
    def __init__(self, level, type):
        self.level = level
        self.type = type

class Python(Language):
    def write_function(self, func_name, arg):
        return f'def {func_name}({arg}):'

    def create_variable(self, var_name, value):
        return f'{var_name} = {value.__repr__()}'
        
class JavaScript(Language):
    def write_function(self, func_name, arg):
        a = '{     }'
        return f'function {func_name}({arg}) {a};'

    def create_variable(self, var_name, value):
        return f'let {var_name} = {value.__repr__()};'

py = Python('mid', 3)
print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))

js = JavaScript('mid', 4)
print(js.write_function('validate', 'form'))
print(js.create_variable('password', 'john@123'))


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

# 8 
class Planet:
    def __init__(self, orbit):
        self.orbit = orbit
    
          
class Mercury(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)
        
    def get_age(self, earth_age):
        res = earth_age * 365 // self.orbit
        return f'на Меркурии ваш возраст составляет {res} лет'


class Venus(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)

    def get_age(self, earth_age):
        res = earth_age * 365 / self.orbit * 365
        return f'на Венере ваш возраст составляет {round(res)} дней'

class Jupiter(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)

    def get_age(self , earth_age):
        res = (earth_age * 365 // self.orbit) * (24 * 365)
        return f'на Юпитере ваш возраст составляет {res} часов'

merc = Mercury(88)
print(merc.get_age(20))
ven = Venus(225)
print(ven.get_age(20))
jup = Jupiter(12)
print(jup.get_age(20))

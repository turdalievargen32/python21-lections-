
# class Purse():
#     balance = 0
#     tax = 10
#     def __init__(self,money):
#         self.money = money 

#     def into(self):
#         result = (self.money + self.balance) / self.tax
#         return result

# obj = Purse(100)
# print(obj.into())


# class Rectangle():

#     color_defalult = 'yellow'

#     def __init__(self,width,leight):
#         self.width  = width
#         self.leight = leight

#     def area(self):
#         return self.width * self.leight


# obj1 = Rectangle(7,21)
# obj2 = Rectangle(2,4)

# print(obj1.area())
# print(obj1.color_defalult)



# class Car:

#     # создание методов класса
#     def start(self):
#         print ("Двигатель заведен")

# car_a = Car()  
# print(car_a)

# class Car:

#     # создание методов класса
#     def __str__(self):
#         return "Двигатель заведен"

# car_a = Car()  
# print(car_a)



# class Class1():
#     def first(self):
#         pass
#     def second(self):
#         pass

# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# print(obj.first())
# print(obj.second())
# print(obj.third())
# print(obj.fourth())

# class A():
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

# class MyDict(dict):
#     def get(self, object):
#         print('Are you kidding?')
#         return super().get(object)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 

# class MyDict(dict):
#     def get(self,key, value):
#         print('Are you kidding?')
#         return super().get(key,value)

# obj_dict = MyDict({'some_title': 2}) 

# print(obj_dict.get('some')) 


# class MyDict(dict):
#     def get(self,key, default):
#         print('Are you kidding?')
#         return super().get(key,default)

# obj_dict = MyDict({'some_title': 2}) 

# print(obj_dict.get('some')) 


# class MyString(str):
#     def append(self,object):
#         return super().append(object)


#     def pop(self, object):
#         return super().pop(object)

# example = MyString('String') 
# example.append('hello') 
# print(example)
# print(example.pop()) 
# print(example) 



# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'name: {self.name}, age: {self.age}'


# class Student(Person):
#     def __init__(self,name,age,faculty):
#         super().__init__(name,age)
#         self.faculty = faculty

#     def display_student(self):
#         person_display = super().display()
#         return f'{person_display}, faculty {self.faculty}'
        


# obj_student = Student('Argo', 18, 'computer science')
# print(obj_student.display()) 
# print(obj_student.display_student()) 

# class Person():
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')


# class Employee(Person):
#     def __init__(self,name,last_name,work,status):
#         super().__init__(name,last_name)
#         self.work = work
#         self.status = status
    
#     def get_info(self):
#         print (f'“Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} и копыта на должности {self.status}')

# class Student(Person):
#     def __init__(self,university,course):
#         super().__init__()
#         self.university = university
#         self.course = course
    
#     def get_info(self):
#         print(f'Привет, меня зовут Иван Петров, я учусь в {self.university} на {self.course} курсе')

# person = Person('Argen', 'Turdaliev')
# employee = Employee('Argen', 'Turdaliev', 'Data scientist', 'Senior')
# student = Student('la Sapienza', 3)

# def get_human_info(obj):
#     print(obj.get_info())

# get_human_info(employee)
# get_human_info(student)
# get_human_info(person)



# class Person():
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'


# class Employee(Person):
#     def __init__(self,name,last_name,work,status):
#         super().__init__(name,last_name)
#         self.work = work
#         self.status = status
    
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} и копыта на должности {self.status}.'

# class Student(Person):
#     def __init__(self, name, last_name, university,course):
#         super().__init__(name,last_name)
#         self.university = university
#         self.course = course
    
#     def get_info(self):
#         return f'Привет, меня зовут Иван Петров, я учусь в {self.university} на {self.course}'

# person = Person('Иван', 'Петров')
# employee = Employee('Иван', 'Петров', 'Рога', 'директор')
# student = Student('Иван', 'Петров' 'КГТУ', 3,'курсе')

# def get_human_info(obj):
#     print(obj.get_info())

# get_human_info(employee)
# get_human_info(student)
# get_human_info(person)




# class OS():
#     def __init__(self,version):
#         self.version = version

# class Windows(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}"  горячими клавишами CTRL + C'

# class MacOS(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'

# class Linux(OS):
#     def copy(self,text):
#         self.text = text 
#         return f'скопирован текст "{self.text}"  горячими клавишами CTRL + SHIFT + C'

# win = Windows(11)
# mac = MacOS(10)
# lin = Linux(2)

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))



# class Money():
#     def __init__(self,country,symbol):
#         self.country = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80 
#     def exchange(self,amount):
#         res =  self.rate * amount
#         return f'$ {res} равен {amount} сомам'

# class Euro(Money):
#     rate = 98.40
#     def exchange(self,amount):
#         res = self.rate * amount
#         return f'€ {amount} равен {res} сомам'


# class A():
#     def method1(self):
#         print('Hello World')
    
# class B(A):
#     def method1(self):
#         super().method1()
#         pass
        
# b1 = B()
# print(b1.method1())


# class Auto():
#     def ride(self):
#         return 'Riding on a ground'

# class Boat():
#     def swim(self):
#         return 'Floating on water'

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()

# obj = Amphibian() 
# print(obj.ride()) 
# print(obj.swim())



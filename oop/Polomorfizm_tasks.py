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







# 1 
class Class1():
    def first(self):
        pass
    def second(self):
        pass

class Class2(Class1):
    def third(self):
        pass
    def fourth(self):
        pass

obj = Class2()
print(obj.first())
print(obj.second())
print(obj.third())
print(obj.fourth())

# 2 
class A():
    def method1(self):
        print('Основной функционал')

class B(A):
    def method1(self):
        super().method1()
        print('Дополнительный функционал')

obj = B()
obj.method1()


# 3 
class MyString(str):
    def __init__(self, value):
        self.value = value
    
    def append(self, string):
        self.value += string

    def pop(self):
        string = self.value
        self.value = self.value[:-1]
        return string[-1]

    def __str__(self):
        return self.value

example = MyString('String') 
example.append('hello')
print(example) 
print(example.pop()) 
print(example) 




# 4
class MyDict(dict):
    def get(self, key, default = 'Are you kidding?'):
        return super().get(key, default)

obj_dict = MyDict({'some_title': 2})

print(obj_dict.get('some'))




# 5 
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f'name:{self.name}, age:{self.age}'


class Student(Person):
    def __init__(self,name,age,faculty):
        super().__init__(name,age)
        self.faculty = faculty

    def display_student(self):
        person_display = super().display()
        return f'{person_display}, faculty:{self.faculty}'
        


obj_student = Student('Rick', 21, 'science')
print(obj_student.display()) 
print(obj_student.display_student()) 

# 6 
class ContactList(list):
    def __init__(self,value=list()):
        self.value = value


    def search_by_name(self,name):
        result = []
        for i in self.value:
            if name in i:
                result.append(i)
        return result
    
all_contacts =  ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya'))

# 7 
class SmartPhones:
    def __init__(self,name,color,memory,battery=0):
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = battery
    
    def __str__(self):
        return f'{self.name} {self.memory}'
    
    
    def charge(self, percent):
        self.battery =+ percent
        return self.battery

class Iphone(SmartPhones):
    def __init__( self,name,color,memory,ios, battery=0):
        super().__init__(name,color,memory,battery)        
        self.ios = ios
        
    def send_imessage(self, message):
        return f'sending {message} from {self.name} {self.memory}'

class Samsung(SmartPhones):
    def __init__(self,name,color,memory,android,battery=0,):
        super().__init__(name,color,memory,battery)
        self.android = android

    def show_time(self):
        from datetime import datetime
        current_time = datetime.now()
        return current_time.time()

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone)
print(phone.battery) 
phone.charge(20) 
print(phone.battery) 
iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time())

#8 
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
    
def check_letters(string):
    if string.isupper():
        return f'ВСЕ ОТЛИЧНО! {string}'
    else:
        raise capitals_error

capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
print(check_letters('HELLO'))


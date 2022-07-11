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

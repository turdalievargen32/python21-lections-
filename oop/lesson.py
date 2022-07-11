class Dog():
    def voice(self):
        print('gav-gav')

dogs = Dog()

dogs.voice()

class Cat:
    def voice(self):
        print('may')


class Bird:
    
    def __init__(self):
        print("Птица готова")

    def whoisThis(self):
        print("Птица")

    def swim(self):
        print("Плывет быстрее")

# дочерний класс
class Penguin(Bird):

    def __init__(self):
        # вызов функции super() 
        super().__init__()
        print("Пингвин готов")

    def whoisThis(self):
        super().__init__()
        print("Пингвин")

    def swim(self):
        print("Бежит быстрее")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()

# Птица готова
# Пингвин готов
# Птица готова
# Пингвин
# Бежит быстрее


# class Person:
#     legs = 2

#     def __init__(self):
#         self.legs = 2


#     def hello(self):
#         print('hello')

# person1 = Person()
# person2 = Person()

# print(person1)



# person1.name = 'Argen'
# Person.a = 10
# print(person1.a)

# print(person1.a, person2.a)



# from abc import ABC, abstractmethod

# class AbstractClass(ABC):
#     a = 5
    
#     @abstractmethod
#     def hello(self):
#         pass

# class A(AbstractClass):
#     def hello(self):
#         print('hello')

# a = A()

"""
Inheritance
"""

# class Human:
#     a = 5
#     def __init__(self, name, last_name) -> None:
#         self.name = name
#         self.last_name = last_name

# class Human2:
#     a = 5
#     def __init__(self, name) -> None:
#         self.name = name


# class Programmer(Human, Human2):
#     pass
    
#     def __init__(self, age, name) -> None:
#         super().__init__(name)
#         super().a
#         self.age = age

# programmer = Programmer('Jaanger', 'Barakanov')


"""
                                ?       ?
                                |       |
                                |       |
                                ?       ?
                                 \     /
                                  \   /
                                    D
"""

# class A:
#     def __init__(self, name) -> None:
#         pass

# class B:
#     def __init__(self, age) -> None:
#         pass

# class C(A, B):
#     a = 5

# def func():
#     for i in range(10):
#         yield i
#         print('hello')

# a = func()

# while True:
#     try:
#         print(next(a))
#     except StopIteration:
#         break


# import json
# with open('test.json', 'w+') as file:
#     res = json.dumps({5: True})
#     file.write(res)
#     file.seek(0)
#     print(file.read())
#     # print(res)


# class A:
#     @classmethod
#     def create_obj(cls):
#         return cls()

#     @staticmethod
#     def add_():
#         return 5 + 5

# a = A()


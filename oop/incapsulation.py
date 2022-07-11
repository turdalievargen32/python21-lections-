'========================Инкапсуляция========================='
# Инкапсуляция - это принцип ООП 
# 1. Сокрытие данных (ограничение доступа к опредкленным методам и классам)
# 2. Сбор всех необходимых для класса и методов и аттрибутов в "капсулу"(класс)


'====================Модификаторы доступа к аттрибутам==========='
# 1. public()
# 2. protected()
# 3. private()

# class A():
#     attr1 = 'public'
#     _attr2 = 'protected'
#     __attr3 = 'private'


# A.attr1 # public
# A._attr2 # protected
# A.__attr3 # AttributeError: type object 'A' has no attribute '__attr3'.

'===================getter / setter==========================='

class Person():
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age < 120 and new_age > 0:
            self.__age = new_age
        else:
            raise Exception('age can not be less than 0 or more then 120')


obj = Person('Argen', 17)
# print(obj.__age)
print(obj.age)
obj.age = 22
print(obj.age)

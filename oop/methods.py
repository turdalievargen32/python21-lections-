'=====================Class, statics, instance methods=============================='
# instance method(метод обьекта) - метод который принимает первым аргументом self(обьект). Вызываем instance методы у обьекта

# class A():
#     def instnance_method(self):
#         print('метод обьекта')

# obj_a = A()
# obj_a.instnance_method()
# A.instnance_method(obj_a) - # вызываем у класса нужно передаьб обьект 



# class methods(методы класса) - метод который принимант первым аргументом cls(обьекта), чтобы создать метод класса, нужно метод задкодировать classmethod

# class A():
#     @classmethod
#     def class_method(cls):
#         print('Метод класса')

# A.class_method()
# A.class_method()
# A().class_method()



class Pizza():
    def __init__(self, radius, *ingredients):
        self.ingredients = ingredients
        self.r = radius

    def cook(self):
        print(f'Пицца размером {self.r} см \nИнгредиенты:\n{self.ingredients}')

    @classmethod
    def pepperoni(cls, r):
        return cls(r, 'pepperoni', 'tomato')

pizza1 = Pizza(30, 'cheese', 'tomato', 'pepperoni')
pizza2 = Pizza.pepperoni(23)
pizza3 = Pizza.pepperoni(45)
pizzas = [pizza1,pizza2,pizza3]
for i in pizzas:
    i.cook()


# static методы - просто функции внутри класса, которые не взамиодействуют ни с классом, ни с обьектом

class Square:
    def __init__(self, a):
        self.a = a 
        self.s = self.get_s(a)

    @staticmethod
    def get_s(a):
        return a ** 2

obj = Square(4)
print(obj.s)

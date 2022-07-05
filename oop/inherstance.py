
"Наследование - принцип ООП, где мы можем в дочернем классе унаследовать преопределять и импользовать все аттрибуты  методы родительского класса"

class A:
    def method(self):
        print('method in class A')

obj_a = A()
obj_a.method() # method in class A

class B(A):
    """Наследовали все методы и аттрибуты у класса A"""

obj_b = B()
obj_b.method() # method in class A

"class A - родительский класс"
"class B - дочерний класс"

class C(A):
    """Мы наследовали все методы и аттрибуты у класса А и переопределили метод method"""
    def method(self):
        print('method in class C')

obj_a = A()
obj_a.method() # method in class A

obj_a = C()
obj_a.method() # method in class C

"Переопределение - даем то же название, но другое значение"


"super() - функция, которая позволяет обратиться к родительскому классу и вызвать определенные методы и аттрибуты"
class A:
    def my_range(selfe, n):
        return list(range(0, n+1))


class B:
    def my_range(self):
        # через super мы оброщаемся к методу родительского класса
        return super().my_range(10)


obj_a = A()
obj_a.my_range(3) # [0,1,2,3]

obj_b = B()
obj_b.my_range() # [0,1,2,3,4,5,6,7,8,9,10]



"======================Виды наследование======================="
# одиночное наследование
# множественное наследование
# многоуровневое наследоване
# иерархическое наследование
# гидридное наследование
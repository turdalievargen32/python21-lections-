"===================Принципы ООП======================"
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация


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

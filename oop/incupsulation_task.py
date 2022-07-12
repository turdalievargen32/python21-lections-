# 1
class A():
    def public(self):
        return 'Public method'
    def _protected(self):
        return 'Protected method'
    def __private(self):
        return 'Private method'

obj1 = A()
print(obj1.public())
print(obj1._protected())
print(obj1._A__private())

# 2 

class A():
    def method1(self):
        print('Hello World')
    
class B(A):
   pass
        
b1 = B()
b1.method1()

# 3

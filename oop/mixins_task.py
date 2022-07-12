# 1 
class Auto():
    def ride(self):
        return 'Riding on a ground'

class Boat():
    def swim(self):
        return 'Floating on water'

class Amphibian(Auto, Boat):
    pass

obj = Amphibian()

obj = Amphibian() 
print(obj.ride()) 
print(obj.swim())

# 2 

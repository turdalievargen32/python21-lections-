"============================словари====================="
# dictionary - изменяемый, итеририуемый, неидексируемый, неупорядочный тип данных, в котором значения храняться в парах(ключ : )Z
#dict_ = {'a':'hello','b':2,'c':3}
print(dict_['b'])
#ключами в словаре могут все неизменяемые типы данных 
# значениями в словаре могут быть любые типы данных
# ключи должны быть уникальными  



dict_ = {1:'hello',
 'a':4, 
 4.5: {'a':5},
 #{'s':5} # TypeError
 }

"========================Методы словарей==================="
dict_.clear() #чистит словарь
print(dict_) #{}

dict = dict_.fromkeys([1,2,3])
print(dict_) #(1:None,2:None,3:None)

dict_ = {"a":2,"a":3,"a":4}
print(dict_) #{'a': 4}
dict_["a":5] 
print(dict_) 

#get мутод get нужен для полученияя значений
dict_ = {"a":1, "b":2}
dict_["a"] #1
dict_["c"] #KeyError

dict_.get("a") #1
dict_.get('c') #None

dict_.keys() #dict_keys(['a', 'b'])
dict_.values() #dict_values([1,2])
dict_.items() # dict_items([('a', 1), ('b', 2)])

dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
# метод updete добовляет пары из второго в первый
dict1.update(dict2) 
print(dict1) # {1:"a", 2:"b", 3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}


# метод pop удаляет пару по ключу и возрващает значение
print(dict1.pop(3)) #d
print(dict1) #{1:"a",2:"b",4"e"}
print(popped) #4 


#  метод popitem удаляет и вовращает последнюю пару
print(dict1.popitem()) # (4,"e")
print(dict1) # [1:"a", 2:"b"]




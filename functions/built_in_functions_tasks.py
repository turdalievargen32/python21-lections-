#task1
list_ = [1, 2, 3, 4]  
result = sum(list_)
print(result)

#task2
list_ = [1, 5, -9, 6, -4] 
result = all(i>3 for i in list_)
print(result)

#task3
list_ = [5, 8, 4, 6, 7]
result = any(i<0 for i in list_)
print(result)

#task4
list_ = [1, 2, 3, 4]  
result = list(map(lambda x: x**2, list_))
print(result)

#task5
list_ = [1, 2, 3, 4] 
result = list(filter(lambda i: i%2==0, list_))
print(result)

#task6
list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
result = list(filter(lambda i: len(i)>7, list_ ))
print(result)

#task7
from functools import reduce
list_ = [5, 6, 7, 8] 
def mul(a, b):
    return a * b

result = reduce(mul, list_)
print(result)

#task8
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
list2 = list(filter(lambda i: i%2==0, list_))
list3 = list(filter(lambda i: i%2!=0, list_))
result = f'even: {len(list2)}, odd: {len(list3)}'
print(result)


#task9
list_ = [-1, 2, 3, 5, -3, 7] 
result = list(map(lambda i: i > 0, list_))
print(result)


#task10


list_ = ['Paul', 'George', 'Ringo', 'John'] 
result = reduce(lambda i,x: i if len(i)>len(x) else x, list_)
print(result)

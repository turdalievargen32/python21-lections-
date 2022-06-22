#task1 
def add(a,b):
    return a+b
res = add(4,5)
print(res)

# task2
def get_string_length(string):
   something = len(string)
   return something 

   #task3
def get_type(a,b):
    print(type(a))
    print(type(b))
res = get_type(5,'a')

#task4
def divide(a,b):
    return a/b
print(divide(10,2))


#task5 
dict_ = {'a':1,'b':2,'c':3}

def dictionary(di):
      for element in di:
          print(element) 
dictionary(dict_)
 
 #task6


#task7
def is_palindrome(string):
    string = string.lower()
    if string[::-1]==string:
        return True
    else:
        return False
print(is_palindrome('довод')) 


#task8
def max_num(a,b):
    if a < b:
        return b
    else:
        return a
print(max_num(15, 10))      

#task9
def multiply_list(list_):
    answer = 1
    for i in list_:
        answer *= i
    return answer
 
print(multiply_list([1, 2, 3, 4, 5]))

#task10


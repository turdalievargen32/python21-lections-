def welcome(name,last_name):
     return f'welcome,{name}, {last_name}'
name = input()
last_name = input()
print(welcome(name,last_name))



def get_words(word):
     list_letters = list(word)
     return list_letters

def lectters(letter):
    good_words = ['a','e','i','o','u','y']
    list_wowels = [i for i in letter if i in good_words]
    return list_wowels
my_word = input('type something')
print(lectters(get_words(my_word)))






def get_words(word):
    list_letters = list(word)
    return list_letters

def lectters(letter):
    good_words = [['a','e','i','o','u','y']]
    list_wowels = [i for i in letter if i in good_words]
    result=''.join(list_wowels)
    return result
    
my_word = input('type something')
print(lectters(get_words(my_word)))


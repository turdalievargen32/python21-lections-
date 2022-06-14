# Task 1

name_of_friends = ['Саша', 'Маша', 'Паша', 'Даша', 'Гоша']

for names in name_of_friends:
    print(names)

# Task 1 (#2)

# for list_ in name_of_friends:
#     for element in list_:
#         print(element, end = '')
#     print()


# Task 2

labels = ['Honda', 'BMW', 'Mercedes']

for cars in labels:
    print(f'I like brand {cars}')

# Task 2 (#2)

# for carlist in labels:
#     print('I like brand ', end = '')
#     for element in carlist:
#         print(element, end = '')
#     print()

# Task 3

name_of_list = ['Hello world!']

half_length = int((len(name_of_list[0])) / 2)

chast1 = name_of_list[0][:half_length]
chast2 = name_of_list[0][half_length:]

if int(len(name_of_list[0])) % 2 != 0:
    half_length = int(len(chast1)) + 1

new_chast1 = name_of_list[0][0:half_length]
new_chast2 = name_of_list[0][half_length:]

new_list = new_chast2 + new_chast1

print(list(new_list))


# Task 4

import copy

list_ = ['1', '2']

new_list = copy.deepcopy(list_)
new_list.reverse()

print(new_list)


# Task 5

suitcase = []

suitcase.append('1')
suitcase.append('2')
suitcase.append('3')
suitcase.append('4')
suitcase.append('5')

fifth = suitcase[-1]
suitcase.remove(fifth)

suitcase.insert(0, '0')

print(suitcase)


# Task 6

nums = [1, 2, 3, 4, 18, 20, 0, 3]
res = []

for num in nums:
    if num < 5:
        res.append(num)

print(res)

# Task 6 (#2)

nums = [1, 2, 3, 4, 18, 20, 0, 3]
res = [num for num in nums if num < 5]

print(res)


# Task 7

info = input()

list_ = list(info)
tuple_ = tuple(info)

print(list_[::2])
print(tuple_[::2])


# Task 8

list_ = [1, 2, 3, 4, 5]
new_list = []

for num in list_:
    num = str(num)
    new_list.append(num)

print(new_list)


# Task 9

list_ = [1, 2, 3, 4, 5]
new_list = []

for num in list_:
    if num % 2 != 0:
        num = 'нечетное'
    else:
        num = 'четное'
    new_list.append(num)

print(new_list)


# Task 10

list_ = list(range(20))
print(list_)


# Task 11

list_ = list(range(0, 101, 2))
print(list_)


# Task 12

list1 = [11, 23, 45, 7, 9]
list2 = [21, 4, 16, 8, 10]

list1.extend(list2)
result = 0

for number in list1:
    result += number  #result = number + result

print(result)


# Task 13

data = input()

list_ = str(data).split(',')
list_.sort()
print(list_)


# Task 14

list_ = [3, 3, 8]

if list_[0] == list_[-1] or list_[0] == list_[1]:
    print('yes')
elif list_[1] == list_[-1]:
    print('yes')
else:
    print('ERROR')

# Task 15

list_ = list(range(54, 9184))
list1 = []

for num in list_:
    if num % 5 == 0:
        list1.append(num)

print(list1)
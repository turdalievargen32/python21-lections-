import random

name = input('What is your name ?: ')
b = input(f'{name},do you want to play ?(Enter Yes или No):  ')
while b == 'Yes':
    for i in range(1, 11):
        g = 11 - i
        print(f'{name}, you have attemps: {g} ')
        r = random.randint(1, 10)
        c = int(input(f'{name}, I guess number from 1 to 20:  '))
        if r == c:
            print(f'{name}, you win! the number was guessed. You spent attemps: {i}')
            break
        else:
            print(f'{name}, You lose!')
            continue
    b = input(f'{name}, do you want to play again ?(Enter Yes or No): ')
print(f'До свидания, {name}!')

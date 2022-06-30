import random

first_time = 0

def hangman():
    hangman = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    ------
    """,
    """
    ------
    |    |
    |    O  
    |
    |
    |
    |
    ------
    """,
    """
    ------
    |    |
    |    O
    |    T
    |
    |
    |
    |
    |
    --------
    """,
    """
    ------
    |    |
    |    O
    |   /T\\
    |
    |
    |
    ------
    """,
    """
    ------
    |    |
    |    O
    |   /T\\
    |    |
    |
    |
    ------
    """,
    """
    ------
    |    |
    |    O
    |   /T\\
    |    |
    |   /
    |
    ------
    """,
    """
    ------
    |    |
    |    O
    |   /T\\
    |    |
    |   / \\
    |
    ------
    """
    )


    max_wrong = len(hangman) - 2
    tries = max_wrong
    words = ("ПОЖАРНЫЙ", "БРЕЙК", "СПОРТ", "МАФИЯ", "НОУТБУК", "ФУТБОЛ", "ПИТОН", "МАШИНА", "ЧАСЫ", "ЕДА")

    word = random.choice(words)

    hidden_word = "*" * len(word)

    wrong = 0
    used = []

    print("\nА вот собственно и сама виселица. Удачи!")

    while wrong < max_wrong and hidden_word != word:
        print(hangman[wrong])
        print("\nИспользованы следующие буквы:\n", used)
        print("\nЗагаданное слово:\n", hidden_word)
        print(f"\nОсталось попыток: {tries}")
        global first_time

        guess = input("Введите букву: ").upper()
        while guess in used:
            expressions = ("Ты уже предлагал букву", "КАМОН! Ты уже предлагал букву")
            print(f"{random.choice(expressions)} '{guess}'")
            guess = input("\n\nВведите букву: ").upper()
        used.append(guess)

        if guess in word:
            print(f"\nДа! Буква '{guess}' есть в слове!")
            new = ""
            for letter in range(len(word)):
                if guess == word[letter]:
                    new += guess
                else:
                    new += hidden_word[letter]
            hidden_word = new
        else:
            print(f"\nБуквы '{guess}' нет в слове!")
            tries -= 1
            print(f"Осталось {tries} попыток")
            wrong += 1
    if wrong == max_wrong:
        print("\nWASTED")
        print('Ты проиграл!')
        print(hangman[-1])
        print(f"Было загадано слово '{word}'.")
        first_time += 1
        new_game()
    else:
        pass
        print("Загаданное слово:\n", hidden_word)
        print("\nМолодец! Ты выиграл!")
        first_time += 1
        new_game()
    
def new_game():
    answer = input ('\nСыграем снова? (да/нет)\n').lower()
    if answer == 'да' and first_time == 0:
        input(
'''
Игра называется "Виселица"
Я загадаю слово, а ты должен по буквам его угадать.
Тебе дается 5 попыток, за каждую ошибку я буду дорисовывать человека на виселице!
От тебя зависит судьба несчастного рисованного человечка!
Введи любую букву или символ, чтобы продолжить.
'''
)
        hangman()
    elif answer == 'да' and first_time > 0:
        print('\n\nОпять ты')
        hangman()
    elif answer == 'нет':
        print('\nНу ладно. Пока!')
    else:
        da_ili_net()

def da_ili_net():
    answer = ''
    while answer not in ('да', 'нет'):
        questions = ("ДА или НЕТ???", 
        "Ты читать не умеешь?!\nЕсли хочешь сыграть пиши - ДА\nЕсли не хочешь - НЕТ", 
        "Так ДА или НЕТ?!")
        random_q = random.choice(questions)
        answer = input(f"\n{random_q}\n").lower()
        if answer == 'да' and first_time == 0:
            input(
'''
Игра называется "Виселица"
Я загадаю слово, а ты должен по буквам его угадать.
Тебе дается 5 попыток, за каждую ошибку я буду дорисовывать человека на виселице!
От тебя зависит судьба несчастного рисованного человечка!
Введи любую букву или символ, чтобы продолжить.
'''
)
            hangman()
        elif answer == 'да' and first_time > 0:
            print('\n\nОпять ты')
            hangman()
        elif answer == 'нет':
            print('\nНу ладно. Пока!')
            break

print("Хочешь сыграть в игру? (да/нет)")

answer = input().lower()

if answer == 'да' and first_time == 0:
    input(
'''
Игра называется "Виселица"
Я загадаю слово, а ты должен по буквам его угадать.
Тебе дается 5 попыток, за каждую ошибку я буду дорисовывать человека на виселице!
От тебя зависит судьба несчастного рисованного человечка!
Введи любую букву или символ, чтобы продолжить.
'''
)
    hangman()
elif answer == 'да' and first_time > 0:
    print('\n\n Снова ты')
    hangman()
elif answer == 'нет':
    print('\nКак хочешь. Пока!')
else:
    da_ili_net()
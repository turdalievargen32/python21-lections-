# 1 
class Song:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author   
        self.year = year 

    def show_title(self):
        return f'Название этой песни {self.title}'

    def show_author(self):
        return f'Автор этой песни {self.author}'

    def show_year(self):
        return f'Эта песня вышла в {self.year} году'

song = Song('18+','egor', '2013')
print(song.show_title())
print(song.show_author())
print(song.show_year())

# 2 
class Circle:
    color = 'Синий'
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.pi * pow(self.radius, 2)

circle = Circle(2)
circle.color = 'Красный'

print(circle.color)
print(circle.get_area())


# 3 
class BankAccount:
    balance = 0

    def withdraw(self, amount):
        self.amount = amount
        BankAccount.balance -= amount
        print(f'Ваш баланс: {BankAccount.balance} сом')

    def deposit(self, amount):
        self.amount = amount
        BankAccount.balance += amount
        print(f'Ваш баланс: {BankAccount.balance} сом')

account = BankAccount()

account.deposit(1000) 
account.withdraw(500)

# 4 

class Taxi:
    def __init__(self, name, cost, cost_km):
       self.name = name
       self.cost = cost
       self.cost_km = cost_km

    def get_total_cost(self, km):
        trip_price = self.cost + self.cost_km * km
        return f'Такси {self.name}, стоимость поездки: {trip_price} сом'

taxi1 = Taxi('Namba', 45, 12)
taxi2 = Taxi('Jorgo', 46, 13)
taxi3 = Taxi('Yandex', 50, 14)

print(taxi1.get_total_cost(5))
print(taxi2.get_total_cost(6))
print(taxi3.get_total_cost(7))


# 5
class Phone:
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone 

    def get_info(self):
        return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'

contact = Phone('Argen','Turdaliev',  '+996706040477')


print(contact.get_info())

#6 

class Salary:
    percent = 8

    def __init__(self, salary, experience):
        self.salary = salary
        self.experience = experience

    def count_percent(self):
        tax_per_month = self.salary / 100 * self.percent
        result = self.experience * tax_per_month
        return result

obj = Salary(10000, 10)

print(obj.count_percent())
    
#7
from datetime import date

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner
    
    def get_year(self):
        current_year = date.today().year
        return f'выиграл {current_year - self.year} лет назад' 

winner1 = Nobel('Литература', 1971, 'Пабло Неруда') 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())
  
winner2 = Nobel('Литература', 1994, 'Кэндзабуро Оэ') 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())



        
# 8
class Password:
    def __init__(self,password):
        self.password = password

    def validate(self):
        if len(self.password) < 8 or len(self.password)>15:
            raise Exception('Password should be longer than 8, and less than 15 ')

        check_number = list(filter(lambda x:x.isdigit, self.password))
        if len(check_number) == 0:
            raise Exception('Password should contain numbers too')
        
        check_letter = list(filter(lambda x:x.isalpha, self.password))
        if len(check_letter) == 0:
            raise Exception('Password should contain letters as well')
        
        check_SYMBOLS = list(filter(lambda x:x in '@#&$%!~*', self.password))
        if len(check_number) == 0:
            raise Exception('Your password should have some symbols')
            
        return "Ваш пароль сохранен."



    def __str__(self):
        pass_leight = len(self.password)
        return pass_leight * '*'

password = Password('ArgenT123@')

print(password.validate())

#8
import math

class Math:
    def __init__(self, value):
        self.value = value
    
    def get_factorial(self):
        fact = math.factorial(self.value)
        return fact

    def get_sum(self):
        num_list = list(map(int, str(self.value)))
        result = sum(num_list)
        return result

    def get_mul_table(self):
        result = ''
        num_list = list(range(1, 11))
        for num in num_list:
            line = self.value * num
            result += f'{self.value}x{num}={line}\n'
        return result

num = Math(11)

print(num.get_factorial())
print(num.get_sum())
print(num.get_mul_table())






#10
class ToDo:
    instances = {}
    
    def __init__(self,todo):
        self.todo =todo


    def give_priority(self,priority):
        self.instances[priority] = self.todo

    def list_of_tasks(self):
        return sorted(list(self.instances.items()), key=lambda todo:todo[0])


todo1 = ToDo('сделать домашку')
todo2 = ToDo('сходить в кино')
todo3 = ToDo('выгулять собаку')

todo1.give_priority(3)
todo2.give_priority(2)
todo3.give_priority(1)
print(ToDo.instances)
print(todo1.list_of_tasks)

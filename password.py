
import random
import pandas as pd

class Account:
    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

class create_account(Account):
    def __init__(self):
        name = str(input())
        surname = str(input())
        date_of_birth = str(input())
        date_of_birth = pd.to_datetime(date_of_birth)

        
        while True:
            print('This is your username')
            username = name[:-3] + surname
            print(username)
            print('This is your password')
            x = random.choice(surname)
            y = random.randint(3, 24) 
            password = name + x + str(y)
            print(password)
            quit()

class log_in(Account):    
    def __init__(self):
        username = input('please insert your username')
        password = input('your password')
        if username == True:
            print('access granted')
            if password == True:
                print('welcome', +" ", + username)
        else:
            print('unable to confirm your username and password')
    def try_again(self):
        return log_in()

lo = Account('name', 'surname', 'date_of_birth')
print(lo)
cr = create_account()
print(cr)
lon = log_in()
print(lon)

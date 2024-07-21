import random

name = input('Enter your name: ')
# you can set the sales to your preference.
sales = 3
# price can be set to your liking
price = "$24.50"


while True:
    tickets = input("Hello welcome!" +" " + name)
    print("tickets price is" +" " + price)
    # generates tickets_ID
    gen_ticket = random.randrange(1, 100, 2 )
    tickets_ID = "".join(random.choices(name[:5] + str(gen_ticket) + name[-3:]))
    if sales > 0:
        print("purchase your tickets here.")
        print('Here is your tickets_ID:', tickets_ID)
        sales = sales - 1
        # ask the user if he/she would like to buy another tickets?.
        try_again = input('would you like to purchase another tickets?')
        if try_again == 'yes':
            print('thanks for your patronage.')
            print(tickets)
        elif try_again == 'no':
            print('Its nice having you with us')
            quit()
        
    else: 
        print('SOLD_OUT')
        break   
        

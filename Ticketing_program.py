
import random

class Ticket:
    name = input('Please enter your name: ')
    sales = 3 #can be set to your preference
    price = "40" #can be set to your preference
    def __init__(self, name, sales, price):
        self.name = name
        self.sales = sales
        self.price = price

    def user_ticket(self, ticket_ID):
        print(f"Hello welcome {self.name}")
        gen_ticket = random.randrange(1, 259, 2)
        print("Here is your event ticket identification")
        ticket_ID = self.name[5:] + str(gen_ticket) + self.name[-3:]
        return ticket_ID
    def user_payment(self, card_number, expiration_date, amount, merchant_id): 
        payment_info = []
        payment_info['card_number'] = input(card_number)
        payment_info['expiration_date'] = input(expiration_date)
        payment_info['amount'] = input(amount)
        payment_info['merchant_id'] = input(merchant_id)
        return payment_info
    
    def total_sales(self):
        while True:
            if self.sales > 0:
                self.sales = self.sales - 1
                print(f"we are delighted to have you with us {self.name}")
            else:
                print("Event sold out")
                break

purchase_ticket = Ticket("name", "sales", "price")
purchase_ticket.user_ticket('ticket_ID')
purchase_ticket.user_payment('card_number', 'expiration_date', 'amount', 'merchant_id')
purchase_ticket.total_sales()

buy_another_ticket = input('would you like to purchase another ticket?')
if buy_another_ticket == 'YES':
    print("Thanks for your patronage")
    print(purchase_ticket)
elif buy_another_ticket == 'NO':
    print("Have a splendid day")
    quit()



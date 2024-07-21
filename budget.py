
class Budget:
    # Initialize the budget with a name and a balance
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    # Define a method to deposit money into the budget
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to {self.name} budget")
    
    # Define a method to withdraw money from the budget
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds in {self.name} budget")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.name} budget")
    
    # Define a method to transfer money from one budget to another
    def transfer(self, other, amount):
        if amount > self.balance:
            print(f"Insufficient funds in {self.name} budget")
        else:
            self.balance -= amount
            other.balance += amount
            print(f"Transferred {amount} from {self.name} budget to {other.name} budget")
    
    # Define a method to display the budget balance
    def show_balance(self):
        print(f"{self.name} budget balance is {self.balance}")
    def percentages(categories):
        total_withdraws = 0
        total = 0
        for category in categories:
            quantity = total_withdraws(category)
            total += quantity
        porcentajes = []
        for category in categories:
            porcen = (total_withdraws(category)/total)
            porcen = (int(porcen * 10) / 10)*100
            porcentajes.append(porcen)
        return porcentajes

# Create instances of the budget class
food = Budget("Food", 100)
clothing = Budget("Clothing", 50)
entertainment = Budget("Entertainment", 20)

# Test the methods
food.deposit(10)
food.show_balance()
clothing.withdraw(15)
clothing.show_balance()
entertainment.transfer(food, 5)
entertainment.show_balance()
food.show_balance()
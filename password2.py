
import string
import random

def password_setter(lenght, Password):
        #setting the pattern 
        # the lenght can be adjusted to any value     
        characts = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        #generating password
        gen_password = "".join(random.choices(characts, k=lenght))

        print(f"Password must be in '{gen_password}' that is, Password must contain an uppercase letter, a lowercase letter, at least one of the following special characters !@#$%^&()?_,<>/.{[]}/\|-+=;:*, a numeric value and must be {lenght} characters long")
        print("Set your password!")

        #special characters
        special_characters = "!@#$%^&()?_,<>/.{[]}/\|-+=;:*"
        #small letters
        small_letters = "abcdefghijklmnopqrstuvwxyz"
        #capital letters
        capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #numbers
        numeric = "0123456789"
        #setting password
        Password = "".join(input("Set Password: "))
        #setting the conditions
        while Password:
                if len(Password) < lenght or len(Password) > lenght:
                        print(f"Password must be {lenght} characters long")
                
                elif not any(c in special_characters for c in Password):
                        print('Password must contain special characters')
                        
                elif not any(i in small_letters for i in Password):
                        print('Password must contain small letters')
                        
                elif not any(j in capital_letters for j in Password):
                        print('Password must contain capital letters')
                        
                elif not any(t in numeric for t in Password):
                        print('Password must contain numeric figures')
                
                else:
                        print(f"Password {Password} set successfully")
                
                
                break
        print('insert password')
        #setting password
        PASSWORD = input('your password: ')

        """this block of code checks if the password is in the same format with the password_setter,
        it will allow you to proceed given the information are accurate else it will stop until the 
        format is correct"""
        if PASSWORD == Password:
                print('continue to buy ticket')
                Answer = input('YES/NO: ')
                if Answer == 'YES':
                        print('proceed')
                elif Answer == 'NO':
                        print('exit')
                        quit()
        else:
                print('set password accordingly')
                quit()
print(password_setter(7, 'Password'))


def event_ID(full_name, ticket_ID):
        full_name = input('surname first follow by other_name: ')
        print(f"Hello welcome {full_name}!")
        gen_ticket = random.randrange(1, 259, 2)
        print("Here is your event ticket identification")
        ticket_ID = full_name[5:] + str(gen_ticket) + full_name[::-3]
        return ticket_ID
print(event_ID('full_name', 'ticket_ID'))


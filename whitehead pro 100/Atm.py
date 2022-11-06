class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("penny = 100")
        print("quarter = 200")
        print("dollar = 300")

    def withdrawl1(self,penny):
        new_amount = 100 - penny
        print("You have withdrawn amount "+str(penny) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,quarter):
        new_amount = 200 - quarter
        print("You have withdrawn amount "+str(quarter) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,dollar):
        new_amount = 300 - dollar
        print("You have withdrawn amount "+str(dollar) + ". Your remaining balance is "+ str(new_amount))        


def main():
    print("Welcome to Big Bank!")
    Account = input("Please enter your acount image or number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Add penny")
        print("2. Add quarter")
        print("3. Add dollar")
        choose = int(input("1. Add penny  2. Add quarter 3. Add dollar: "))
        if (choose == 1):
           knuts = int(input("Enter the amount:- "))
           new_user.withdrawl1(penny)
        if (choose == 2):
           sickles = int(input("Enter the amount:- "))
           new_user.withdrawl2(quarter)    
        if (choose == 3):
           galleon = int(input("Enter the amount:- "))
           new_user.withdrawl3(dollar)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
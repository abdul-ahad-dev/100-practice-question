class ATM:

    # Constructor
    # special/magic/dunder method
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        # self.menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin
        if type(new_pin) == str:
            print("pin changed")
        else:
            print("Not allowed")

    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create pin 
        2. Enter 2 to deposit 
        3. Enter 3 to withdraw 
        4. Enter 4 to check balance 
        5. Enter 5 to exit 
        
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            exit()

    def create_pin(self):
        self.__pin = input("Enter to set a 4 digit pin : ")
        print("Pin setup successfully")

    def deposit(self):
        temp = input("Enter your pin : ")
        if self.__pin == temp:
            amount = int(input("Enter amount to deposit : "))
            self.__balance = self.__balance + amount
            print("Operation successfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if self.__pin == temp:
            amount = int(input("Enter amount to withdraw cash : "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation successfully")
            else:
                print("Your current balance is not enough to withdraw cash!!")
        else:
            print('Invalid Pin')

    def check_balance(self):
        temp = input("Enter your pin:")
        if self.__pin == temp:
            print("Your current account balance is : ", self.__balance)
        else:
            print("invalid pin")


user = ATM()
while True:
    user.menu()

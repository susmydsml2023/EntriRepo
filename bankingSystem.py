
class BankSystem():
    # Dictionary for customer details
    customer_details = {
        "Susmy": {"password": "susmy123@", "balance": 0},
        "Sagar": {"password": "sagar123@", "balance": 5000 },
        "Sruthy": {"password": "sruthy123@", "balance": 600 }
    }

    # account balance
    def accountBalance(self):
        bal=self.customer_details[username]["balance"]
        print("Your account balance is : Rs.",bal)

    # withdraw
    def withdraw(self):
            print("************WITHDRAW*************")
            withdrawAmount = int(input("How much would you like to withdraw? "))
            bal = self.customer_details[username]["balance"]
            if withdrawAmount > bal:
                print("Insufficient balance")
            else:
                bal = bal - withdrawAmount
                newbalance=bal
                self.customer_details[username]["balance"]=newbalance
                print(f"Rs.{withdrawAmount} is debited from your account")
    #   deposit
    def deposit(self):
            print("************DEPOSIT*************")
            depositAmount = int(input("How much would you like to deposit? "))
            bal = self.customer_details[username]["balance"]
            bal= bal+depositAmount
            newbalance = bal
            self.customer_details[username]["balance"] = newbalance
            print(f"Rs.{depositAmount} is credited to your account")

    #     password change
    def changepassword(self):
        new_password1=input("Enter your new password\t:")
        new_password2=input("Re enter your password\t:")

        if new_password1 == new_password2:
            self.customer_details[username]["password"] = new_password1
            print("Password changed successfully!")
        else:
            print("Password entered do not match. Try again")

#object created for banking system
bank= BankSystem()

#FUNCTION TO DISPLAY THE MENU
def menu():
    while True:
        user_response=int(input(("-----------Enter your Choice-------------\n>Press 1 for Amount Deposit\n>Press 2 for Amount Withdrawal\n>Press 3 for Account Balance\n>Press 4 for Change Password\n>Press 5 for Exit\n")))
        if user_response == 1:
            bank.deposit()
        elif user_response == 2:
            bank.withdraw()
        elif user_response == 3:
            bank.accountBalance()
        elif user_response == 4:
            bank.changepassword()
        else:
           exit()

#ACCOUNT LOGIN
while True:
    print("******Welcome to the Banking System******")
    username=input("Enter your username\t:")
    password=input("Enter your password\t:")

    if username in bank.customer_details and bank.customer_details[username]["password"]==password:
        print("Login Successsfully")
        menu()
    else:
        print("Incorrect username or password")
        request=input("Do you want to change password?YES/NO?")
        if request =="YES":
            bank.changepassword()
        else:
            continue




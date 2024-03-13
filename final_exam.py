import datetime

class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

class Client(User):
    def __init__(self, username, password, bank) -> None:
        super().__init__(username, password)
        self.balance = 0
        self.bank = bank
        self.history = []

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.bank.total_balance += amount
            self.history.append(f'\nDeposited {amount} Tk on {datetime.datetime.now()}.\n')
            print(f'\nSuccessfully deposited {amount} Tk on your account\n.')
            
        else:
            print(f'\nUnacceptable {amount} Tk, please deposit more than 0 Tk.\n')

    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
            self.bank.total_balance -= amount
            self.history.append(f'\nWithdrawn {amount} Tk on {datetime.datetime.now()}.\n') 
            print(f"Withdraw {amount} Tk done!")
        else:
            print(f"Insufficient balance!")

    def check_balance(self):
        return f"You have {self.balance} Tk on your account"
    
    
    def transfer_balance(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f'\nTransferred {amount} Tk on {datetime.datetime.now()}\n.')
            print(f'\nSuccessfully transferred {amount} Tk.\n')
            
        else:
            print(f'\nYou do not have sufficient balance to transfer.\n')
    
    
    def loan(self, amount):
        if amount <= 2*self.balance:
            self.balance += amount
            self.bank.total_balance += amount
            self.bank.total_loan += amount
            self.history.append(f'\nLoan {amount} Tk on {datetime.datetime.now()}\n')
            print(f'\nLoan {amount} Tk added on your account.\n')

        else:
            print(f'\nYou are unable to loan {amount} Tk.\n')
            
    
    def transaction_history(self):
            print(f"Transaction history of {self.username}, ")
            print()
            for transaction in self.history:
                print()
                print(transaction)
                print()






class Bank:
    def __init__(self, bank) -> None:
        self.name = bank
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True

    def check_total_balance(self):
        return self.total_balance

    def check_total_loan(self):
        return self.total_loan

    def enable_loan_feature(self):
        self.loan_feature = True
        
    def disable_loan_feature(self):
        self.loan_feature = False
        
        
   
   
        
        
        
class Admin(User):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        
    def check_total_balance(self, bank):
        return bank.check_total_balance()

    def check_total_loan(self, bank):
        return bank.check_total_loan()

    def enable_loan_feature(self, bank):
        bank.enable_loan_feature()

    def disable_loan_feature(self, bank):
        bank.disable_loan_feature()    
    
    
    
class Main(Client):
    def __init__(self):
        self.users = []
        self.admins = []
        self.bank = Bank("XYZ Bank Ltd.")

    def create_account(self):
        
        print('1.Create User Account\n2.Create Admin Account\n')
        a = int(input("Enter your choice : "))
        if a == 1:
            name = input("Enter Username : ")
            password = input("Enter a password : ")
            self.client_account = Client(name, password, self.bank)
            self.users.append(self.client_account)
            print("\nCongrats, user account created successfully!")
            
        elif a==2:
            name = input("Enter Username : ")
            password = input("Enter a password : ")
            self.admin_account = Admin(name, password)
            self.admins.append(self.admin_account)
            print("\nCongrats, admin account created successfully!")
            
    
    def user_data(self, user):
        while True:
            print(f"\n-------------Welcome to the {self.bank.name}-------------\n")
            print('1.Deposit\n2.Withdraw\n3.Check Balance\n4.Transfer Balance\n5.Loan Balance\n6.Transaction History\n7.Exit\n')
            
            a = input("Enter your choice : ")
            
            if a == "7":
                break
            
            elif a == "1":
                amount = int(input("Enter you deposit amount : "))
                user.deposit(amount)


            elif a == "2":
                amount = int(input("Enter your withdraw amount : "))
                user.withdraw(amount)
                    
            elif a == "3":
                balance = user.check_balance()
                print("\nYou have ",balance," on your account!")
                
            elif a=="4":
                amount = int(input("Enter your transfer amount : "))
                user.transfer_balance(amount)
                    
            elif a=="5":
                if self.bank.loan_feature:
                    amount = int(input("Enter your loan amount : "))
                    user.loan(amount)
                else:
                    print("Currently loan feature isn't available!")
                    
            elif a=="6": 
                user.transaction_history()
                
    
    
    def admin_data(self, admin):
        while True:
            print(f"\n-------------Welcome to the {self.bank.name}-------------\n\n")
            print('\n1.Total Available Balance\n2.Total Loan Amount\n3.Active Loan Feature\n4.Disable Loan Feature\n5.Exit')

            b = input("Enter your choice : ")
            if b == "5":
                break
            
            elif b=="1":
                balance = admin.check_total_balance(self.bank)  # Pass the bank object
                
                print("\nYou have total ",balance, " Tk on your bank")
                

            elif b=="2":
                loan = admin.check_total_loan(self.bank)
               
                print("\nYour bank loaned total ",loan, " Tk to the client!")
               

  
            elif b=="3":
                admin.enable_loan_feature(self.bank)
               
                print("\nLoan Feature Activated!")
               
                
            elif b=="4":
                admin.disable_loan_feature(self.bank)
                
                print("\nLoan Feature Disabled")
                
                
                
                
                
                
    def user_search(self, username, password):
        for u in self.users:
            if u.username == username and u.password == password:
                return u
        return None
    
    
    def admin_search(self, username, password):
        for a in self.admins:
            if a.username == username and a.password==password:
                return a
        return None 
    
    
    def login(self):
        username = input("Enter you username : ")
        password = input("Enter your password : ")
        
        user = self.user_search(username, password)
        admin = self.admin_search(username, password)
        
        
        if user:
            self.user_data(user)
        elif admin:
            self.admin_data(admin)
        else:
            print("First create an account and then try to log in, Thank You!")
            
            
                                 
b = Main()
while True:         
    print("1.Create an Account\n2.Login to your Account\n3.Exit\n")
    c = int(input("Enter Your choice : "))
    if c ==3:
        break
    elif c ==1:
        b.create_account()
    elif c ==2:
        b.login()

   
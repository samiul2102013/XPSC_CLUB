class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.balance = 0
        self.history = []
        self.loan_amount =0

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f'{amount} is has been deposited')

    def withdrawal(self, amount):
        self.balance -= amount
        print(f'You withdrew {amount}. Your current balance is {self.balance}')
        self.history.append(f'{amount} hass been withdrawded')

    def check_balance(self):
        print(f'Your current balance is {self.balance}')

    def get_balance(self, amount):
        self.balance += amount
        self.history.append(f'{amount} tranred money has added')

    def transfer_money(self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.get_balance(amount)
        else:
            print('Insufficient balance')
        self.history.append(f'{amount} has been tranfered')
    
    def transaction_history(self):
        for i in self.history:
            print(i)
    
    def take_loan(self,amount):
        if admin.loan_feature_on:
            if self.balance*2 >= amount:
                self.balance -= amount
                self.loan_amount += amount
                self.history.append(f'{amount} take loan taken')
            else:
                print("not sufficient balance to take loan")

        else:
            print('loan feature is turened off')


class admin:
    loan_feature_on=True
    def __init__(self,name) -> None:
        self.name = name
        self.bank_balnace = 0
        self.users = []
    
    def add_user(self,user):
        self.users.append(user)
    
    def see_total_loan_amount(self):
        total_loan_amount =0
        for i in self.users:
            total_loan_amount += i.loan_amount
        return total_loan_amount
    
    def total_bank_balance(self):
        print(self.bank_balnace)


#user
sam = User('Samiul', 'sami@example.com')
sam.deposit(500)
sam.withdrawal(250)

dam = User('Dam', 'dam@example.com')
dam.deposit(500)

#admin
admin = admin('boss')
admin.add_user(sam)
admin.add_user(dam)

sam.transfer_money(dam, 100)

print(sam.balance)
sam.take_loan(50)
sam.transaction_history()
print(sam.balance)
print(dam.balance)
k=admin.see_total_loan_amount()
print(k)
admin.loan_feature_on = False
dam.take_loan(10)
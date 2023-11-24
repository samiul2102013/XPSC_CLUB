class user:
    def __init__(self,name,admin_instance) -> None:
        self.name = name
        self.money = 0
        self.admin_instance = admin_instance
    
    def diposite(self,amount):
        self.money +=amount
        self.admin_instance.add_money(amount)

    
    def loan(self,amount):
        self.money -= amount
    
class admin:
    def __init__(self,name,money) -> None:
        self.name = name
        self.total_money = money
        self.user = []
    
    def add_money(self,amount):
        self.total_money += amount
    
    def total(self):
        print(self.total_money)


admin = admin('dada',15000)
sam = user('sam',admin)
sam.diposite(500)

dam = user('da',admin) 
dam.diposite(10)

print(admin.total())

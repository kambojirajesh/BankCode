class ATM:
    CardName="SBI"
    def __init__(self,CardNumber,pin,balance=0):
        self.CardNumber=CardNumber
        self.pin=pin
        self.balance=balance

    def display(self):
        print("total amount: ",self.balance)



    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
            print("deposited amount: ",amount)


    def WithDraw(self,amount):
        if amount>0:
            self.balance-=amount
            print("with draw amount: ",amount)

obj=ATM(123456789,5566)
obj.display()
obj.deposit(1000)
obj.WithDraw(500)
obj.display()

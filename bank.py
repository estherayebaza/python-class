class BankAccount:
    def __init__(self,accountNumber,amount,AccountOwner):
        self.accountNumber=accountNumber
        self.amount=amount
        self.AccountOwner=AccountOwner
    def deposit(self):
        print(f"{self.AccountOwner} has deposited {self.amount}")
    def withDraw(self):
        return f" You have withdrawn {self.amount}"
    
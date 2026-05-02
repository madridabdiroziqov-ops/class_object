class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self.a_n = account_number
        self.o = owner
        self.b = balance

    def deposit(self, amount: float):
        self.b+=amount
        print(self.b)

    def withdraw(self, amount: float):
        self.b-=amount
        print(self.b)

    def get_balance(self):
        return self.b

    def __str__(self):
        return f"{self.a_n}, {self.o}, {self.b}"

hisob = BankAccount(account_number="12345", owner="Ali Karimov")
hisob.deposit(500000)
hisob.withdraw(200000)
hisob.get_balance()
print(hisob)
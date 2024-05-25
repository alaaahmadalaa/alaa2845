class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def get_balance(self):
        return self.balance


# إنشاء مثيل من BankAccount
account1 = BankAccount("123456", "Alice")
account1.deposit(1000)
print(f"الرصيد الحالي بعد الإيداع: ${account1.get_balance()}")
account1.withdraw(500)
print(f"الرصيد الحالي بعد السحب: ${account1.get_balance()}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"الرصيد الحالي: ${self.balance}، سعر الفائدة: {self.interest_rate}"


# إنشاء مثيل من SavingsAccount
savings_account = SavingsAccount("789012", "Bob", 0.05)
savings_account.deposit(2000)
savings_account.apply_interest()
print(savings_account)

class BankAccount:
    def __init__(self, bal):
        self.__balance = bal
    def amountmonth(self, amount):
        self.__balance += amount
    def lostamount(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print('Успешно!')
        else:
            print('Ошибка:Недостаточно средств')
    def getbalance(self):
        return self.__balance
    def __str__(self):
        return f'У вас на счету ${self.getbalance():,.0f}'
from bankaccount import BankAccount
def main():
    balance = float(input('Какая сумма у вас на счету? : '))

    saves = BankAccount(balance)

    pay = float(input('Сколько вы получили на этой неделе? : '))
    print('Вношу эти деньги на счет...')
    saves.amountmonth(pay)
    print(saves)


    cash = float(input('Сколько вы желаете снять? : '))
    print('Пытаюсь снять данную сумму с вашего кошелька...')
    saves.lostamount(cash)
    print(saves)

if __name__ == '__main__':
    main()
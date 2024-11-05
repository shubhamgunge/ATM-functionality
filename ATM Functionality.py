def show_Account_Balance(pin,ac_balance,user_pin):
    if user_pin==pin:
        print(f'your current account balnce is {ac_balance}')

    else:
        print('invalid pin')


def show_cash_Deposit(pin,user_ac_no,ac_num,ac_balance):
     if user_ac_no==ac_num:
         n2000=int(input('2000 * '))
         n500 = int(input('500 * '))
         n200 = int(input('200 * '))
         n100 = int(input('100 * '))

         total= 2000*n2000 + 500*n500 + 200*n200 +100*n100

         print(f'Total {total} cash are successfully deposite ')
         print(f'your current balance is ={total-ac_balance}')


def show_cash_withdrawl(pin,user_pin,ac_balance):
    if user_pin==pin:
        cash=int(input('Enter cash Withdrawal:'))
        if cash<ac_balance:
            if cash<25000:
                print(f'you cannot withdrawal more than {ac_balance}')
            print(f'collect your cash = {cash}')
        else:
            print('Insufficient Balance')


def pin_change(pin,user_pin):
    if user_pin==pin:
        new_pin= input('Enter new pin:')
        re_new_pswd= input('Enter pin again:')

        if re_new_pswd==new_pin:
            print("Pin sucessfully changed")

        else:
            print('the recent pin is incorrect')


    else:
        print('incorrect pin')

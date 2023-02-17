# Напишите функцию для транспонирования матрицы


 #def trans_matrix (matrix:list[list])->list[list]:
 #   new_matrix=[[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
 #   for i in range(len(matrix)):
 #       for j in range(len(matrix[0])):
 #           new_matrix[j][i]=matrix[i][j]
 #   return new_matrix

 #item = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
 #res = trans_matrix(item)
 #for i in item:
 #   print(i)
 #print('*'*25)
 #for i in res:
 #   print(i)

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

 #def dict_revers (my_dict:dict)->dict:
 #   res = {}
 #   for key,value in my_dict.items():
 #       value=str(value)
 #       if value==list or tuple:
 #           value="".join(map(str,value))
 #       res.setdefault(value,key)
 #   return res


 #new_dict = {1:'ddsds','jfjf':11,3.14:123,2332:[1,2,3],'kgll':(1,2,3),1:'jdjdj'}
 #on_print = dict_revers(new_dict)
 #print(new_dict)
 #print(on_print)


# Напишите программу банкомат
# - начальная сумма равна 0
# - допустимые действия: пополнить, снять, выйти
# - суммы пополнения и снятия кратны 50 у.е.
# - процент за снятие - 1.5% от суммы снятия но не менее 30 и не более 600 у.е.
# - после каждой третьей операции пополнения или снятия начисляются проценты - 3%
# - Нельзя снять больше чем на счете
# - При превышении суммы в 5 млн,вычитать налог на богатство 10% перед каждой операцией,
# даже ошибочной
# - любое действие выводит сумму денег


from decimal import Decimal
start = True
balance=Decimal('0')
money=Decimal('0')
interest_calculation_count=0

def get_balance():
    global balance
    print(f'Your balance: {balance} c.u.')


def input_command() -> str:
    comand = input('Input command: "top up" or "take off" or "exit": \n')
    return comand


def exit_function():
    global start
    start = False



def enter_money():
    global money
    invalid_input = 'Invalid input. Please enter a multiple of 50: \n'
    spam = input('Enter a multiple of 50: \n')
    while not spam.isdigit() or int(spam)%50!=0:
        spam = input(invalid_input)    
    money = Decimal(spam)


def comission()->Decimal:
    global money
    BID=Decimal(0.015)
    comis=money*BID
    if comis<30:
        comis=30
    elif comis>600:
        comis=600
    print(f'Your comission: {comis}')
    return Decimal(comis)
    


def wealth_tax():
    global balance
    if balance>5000000:
        tax=balance*Decimal(0.1)
        balance=balance-tax
        print(f'Your wealth tax: {tax} c.u.')

            
def top_up_function():
    global balance
    global money
    global interest_calculation_count
    enter_money()
    balance+=money
    money=0
    get_balance()
    interest_calculation_count+=1


def take_off_function():
    global balance
    global money
    global interest_calculation_count
    enter_money()
    comiss=comission()
    if balance>money+comiss:
        balance-=(money+comiss)
        get_balance()
    else:
        print('insufficient funds')
        get_balance()
    money=0
    interest_calculation_count+=1



def interest_calculation():
    global balance
    global interest_calculation_count
    if interest_calculation_count==3:
        BID=Decimal('0.03')
        bid_money=balance*BID
        balance=bid_money+balance
        print(f'interest calculation: {bid_money}')
        get_balance()
        interest_calculation_count=0
    
    

def command_handler(comand: str):
    match comand:
        case 'top up':
            wealth_tax()
            top_up_function()
        case 'take off':
            wealth_tax()
            take_off_function()
        case 'exit':
            exit_function()
        case _: 
            wealth_tax()
            print('try again')



while start:
    command = input_command()
    command_handler(command)
    interest_calculation()

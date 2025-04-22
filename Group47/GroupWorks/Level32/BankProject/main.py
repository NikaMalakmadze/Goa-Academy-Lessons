
from BankDatabase import get_data_from_database, add_user, check_if_account_exsits, get_data_from_user, add_card, get_cards_from_user, get_data_from_database, check_if_card_exsists, get_card_balance, deposit_on_card, withdraw_on_card, get_info_from_user
from IdGenerators import User_ID_generator, Card_ID_generator

from currency_converter import CurrencyConverter
from termcolor import colored
import humanize
import time
import os

def Main_page():
    os.system('clear')
    print(colored("*" * 100, 'green'))
    print(colored('Bank'.center(100), 'dark_grey'))
    print(colored("*" * 100, 'green'))

    print(' '*5,"1) Create Account")
    print(' '*5,"2) Login in to accaount")
    print(' '*5,"3) Exit", '\n')
    
    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        create_account()
    elif main_choice == "2":
        login_account()
    elif main_choice == "3":
        exit(0)
    else:
        print(colored("Not valid input", 'red'))
        time.sleep(3)
        Main_page()

def create_account():
    os.system('clear')
    print(colored("*" * 100, 'blue'))
    print(colored('Account Creation'.center(100), 'dark_grey'))
    print(colored("*" * 100, 'blue'))

    print('Please Enter Your Personal Data!')

    name = input("Enter your name: ")
    lastname = input("Enter your surname: ")

    try:
        BornYear= int(input("Enter your bornyear: "))
    except:
        print(colored('Invalid Born Year!', 'red'))
        time.sleep(2)
        Main_page()

    if BornYear > 2007 or BornYear <= 1900:
        print('\n',' '*5, colored("You are UnderAge!", 'red'))
        time.sleep(3)
        Main_page()
    
    email = input("Enter Email: ").strip()

    if "@" not in email:
        print(colored('Invalid email!', 'red'))
        time.sleep(2)
        Main_page()

    database_emails = get_data_from_database('mail', 'accounts')

    if email in database_emails:
        print(colored('This account already exists!', 'red'))
        time.sleep(3)
        Main_page()

    password = input("Enter Password: ")

    User_ID = User_ID_generator()

    database_Ids = get_data_from_database('User_ID', 'accounts')

    while User_ID in database_Ids:
        User_ID = User_ID_generator()

    User_info = [User_ID, name, lastname, BornYear, email, password]

    add_user(User_info)

    print(colored('Successfuly Created Your account!', 'light_green'))
    time.sleep(3)
    
    Main_page()

def login_account():
    os.system('clear')
    print(colored("*" * 100, 'light_yellow'))
    print(colored('Login in to account'.center(100), 'dark_grey'))
    print(colored("*" * 100, 'light_yellow'))

    print('Please enter your Personal Data!', '\n')

    log_email = input('Enter Email Here(Q): ')

    if log_email == 'q':
        Main_page()
    
    log_password = input('Enter password Here(Q): ')
    
    if log_password == "q":
        Main_page()

    account_finded = check_if_account_exsits(log_email, log_password)

    if not account_finded:
        print(colored('This account Does not exsists!', 'red'))
        time.sleep(3)
        Main_page()

    User_account(log_email)

def User_account(email):

    User_ID = get_data_from_user('User_ID', email)
    name = get_data_from_user('name', email)
    lastname = get_data_from_user('lastname', email)
    year = get_data_from_user('Year', email)
    password = get_data_from_user('password', email)

    os.system('clear')
    print(colored('*'*100, 'light_cyan'))
    print(colored(f'Welocome to your Bank account {name} {lastname}!'.center(100), 'dark_grey'))
    print(colored('*'*100, 'light_cyan'))

    print('What You Would like to do:'.center(20))

    print(' '*5 , '1) Show Account info')
    print(' '*5 , '2) add Card')
    print(' '*5 , '3) withdraw money')
    print(' '*5 , '4) deposit money')
    print(' '*5 , '5) transfer money')
    print(' '*5 , '6) money conversion')
    print(' '*5 , '7) exit from account')

    print('\n', 'Please Enter Your Choice!')

    user_choice = input('Enter Here: ')

    if user_choice == '1':
       account_info_page(User_ID, year, email, password)
       
    elif user_choice == '2':
        add_card_page(User_ID, email)

    elif user_choice == '3':
        withdraw_page(User_ID, email)    
    
    elif user_choice == '4':
        deposit_page(User_ID, email)
    
    elif user_choice == '5':
        transfer_page(User_ID, email)

    elif user_choice == '6':
        conversion_page(User_ID, email)

    elif user_choice == '7':
        Main_page()

    else:
        print(colored("Not valid input", 'red'))
        time.sleep(3)
        User_account(email)

def account_info_page(user_id, Year, email, password):
    os.system('clear')
    print(colored('*'*100, 'green'))
    print(colored('Your account info'.center(100), 'dark_grey'))
    print(colored('*'*100, 'green'))

    print('Your Personal Information!')

    print(' '*5 , f'YOUR ID: {user_id}')
    print(' '*5 , f'YOUR AGE: {2025 - Year}')
    print(' '*5 , f'YOUR MAIL: {email}')
    print(' '*5 , f'YOUR PASSWORD: {password}')

    print('\n','Binded Cards:', '\n')

    user_cards = get_cards_from_user(user_id)
                        #1                                        #2
    # [(user_id, card_id, card_type, balance), (user_id, card_id, card_type, balance)]
    # []

    if len(user_cards) != 0:
        
        information = ["User_ID", "Card_ID", "Card_Type", "Balance"]

        nomer = 1

        for card in user_cards:
            for info, card_data in zip(information, card):
                print(' '*5, f'Your Card {nomer} {info}: {card_data}')         
            nomer += 1
            print()       
  
    else:
        print(colored('No cards Binded! Please add one', 'red'), '\n')
            
    print(' '*4 ,'0. GO BACK')

    info_choice = input('\n     Input Here: ')

    if info_choice == '0':
        User_account(email)
    
    else:
        print(colored('INVALID INPUT!', 'red'))
        account_info_page(user_id, Year, email, password)

def add_card_page(User_ID, email):

    os.system('clear')
    print(colored('*'*100, 'yellow'))
    print(colored('CREATE CARD'.center(100), 'dark_grey'))
    print(colored('*'*100, 'yellow'))

    print('Lets add your Card!'.center(20))
    print('Only Supporting MASTERCARD and VISA!'.center(20))
    print('\n',' '*4 ,'0. Go back')

    print()

    card_type = input('Enter Here(q): ').strip().lower()

    if card_type == 'q':
        User_account(email)

    while card_type not in ['visa', 'mastercard']:
        card_type = input('Enter Valid Card type Here(q): ').strip().lower()
        if card_type == 'q':
            User_account(email)

    card_exists = check_if_card_exsists(User_ID, card_type)

    if not card_exists:

        Card_ID = Card_ID_generator()
    
        database_Cards = get_data_from_database('card_ID', 'cards')
    
        while Card_ID in database_Cards:
            Card_ID =Card_ID_generator()
    
        Card_info = [User_ID, Card_ID, card_type, 0]
    
        add_card(Card_info)
        
        print('\n',colored('Successfuly Binded Card!', 'green'))

        add_card_choice = input('Enter Here(Q): ')

        while add_card_choice != 'q':
            add_card_choice = input('Enter Here(Q): ')
        
        User_account(email)
    
    else:
        print(colored('This card is already binded!', 'red'))
        time.sleep(3)
        User_account(email)

def withdraw_page(User_ID, email):
    os.system('clear')
    print(colored('*'*100, 'cyan'))
    print(colored('Withdraw Page!'.center(100), 'cyan'))
    print(colored('*'*100, 'cyan'))

    print('Enter card to withdraw money: '.center(20))

    withdraw_card_type = input('Enter Here(Q): ').lower()

    if withdraw_card_type == "q":
        User_account(email)

    while withdraw_card_type not in ["visa", "mastercard"]:
        withdraw_card_type = input('Enter Valid Card type Here(q): ').strip().lower()
        if withdraw_card_type == 'q':
            User_account(email)

    withdraw_check_card_exsists = check_if_card_exsists(User_ID, withdraw_card_type)

    if withdraw_check_card_exsists:
        
        withdraw_balance = float(get_card_balance(User_ID, withdraw_card_type))

        print(f'Balance on Your {withdraw_card_type} card: {withdraw_balance} USD'.center(20))

        withdraw_amount_input = input('Please enter how much to Withdraw: ').strip()

        withdraw_amount = ''.join(filter(lambda char: char.isdigit(), withdraw_amount_input))
                                        
        if not withdraw_amount:
            print(colored('Can not Withdraw this value!', 'red'))
            time.sleep(3)
            User_account(email)
        
        else:

            if float(withdraw_amount) > withdraw_balance:
                print(colored('Can not Withdraw more then you have!', 'red'))
                time.sleep(3)
                User_account(email)

            withdraw_on_card(User_ID, withdraw_card_type, float(withdraw_balance), float(withdraw_amount))

            print(colored('Successfuly Withdrawed!          | 0. Exit |', 'green'))

            withdraw_exit = input('     Input Here: ')

            while withdraw_exit != '0':
                withdraw_exit = input('     Input Here: ')

            User_account(email)
    else:
        print(colored('This card is not binded!', 'red'))
        time.sleep(2)
        User_account(email)
    
def deposit_page(User_ID, email):
    os.system('clear')
    print(colored('*'*100, 'light_green'))
    print(colored('Deposit Page!'.center(100), 'dark_grey'))
    print(colored('*'*100, 'light_green'))

    print('Enter card to deposit money: '.center(20))

    deposit_card_type = input('Enter Here(q): ').lower()

    if deposit_card_type == "q":
        User_account(email)

    while deposit_card_type not in ['visa', 'mastercard']:
        deposit_card_type = input('Enter Valid Card type Here(q): ').strip().lower()
        if deposit_card_type ==  'q':
            User_account(email)

    deposit_check_card_exsists = check_if_card_exsists(User_ID, deposit_card_type)

    if deposit_check_card_exsists:

        deposit_balance = float(get_card_balance(User_ID, deposit_card_type))

        print(f'Balance on Your {deposit_card_type} card: {deposit_balance} USD'.center(20))

        deposit_amount_input = input('Please enter how much to Deposit: ').strip()

        deposit_amount = ''.join(filter(lambda char: char.isdigit(), deposit_amount_input))
                                        
        if not deposit_amount:
            print(colored('Can not deposit this value!', 'red'))
            time.sleep(3)
            User_account(email)
        
        else:

            deposit_on_card(User_ID, deposit_card_type, float(deposit_balance), float(deposit_amount))

            print(colored('Successfuly Deposited!          | 0. Exit |', 'green'))

            deposit_exit = input('     Input Here: ')

            while deposit_exit != '0':
                deposit_exit = input('     Input Here: ')

            User_account(email)

    else:
        print(colored('This card is not binded!', 'red'))
        time.sleep(2)
        User_account(email)

def transfer_page(User_ID, email):
    os.system('clear')
    print(colored('*'*100, 'light_green'))
    print(colored('Transfer Page!'.center(100), 'dark_grey'))
    print(colored('*'*100, 'light_green'))

    print('Only Supporting MASTERCARD and VISA!'.center(20))

    transfer_card_type = input("Enter card to transfer money(Q): ").lower().strip()

    if transfer_card_type == 'q':
        User_account(email)

    if transfer_card_type not in ['visa', 'mastercard']:
        print(colored('Please Enter valid card type!', 'light_red'))
        time.sleep(2)
        User_account(email)

    check_transfer_card_exsist = check_if_card_exsists(User_ID, transfer_card_type)

    if not check_transfer_card_exsist:
        print(colored('This card is not binded!', 'red'))
        time.sleep(3)
        User_account(email)
    
    print()

    transfer_to_User_ID = input('Please enter User ID you want to transfer money: ').strip()

    transfer_User_IDs_list = get_data_from_database('User_ID', 'accounts')    # id-s in database ['id','id','id','id','id',]

    if transfer_to_User_ID not in transfer_User_IDs_list:
        print(colored('This User Does not exsists!', 'red'))
        time.sleep(3)
        User_account(email)

    to_user_info = get_info_from_user(transfer_to_User_ID)

    print(f'User That you inputed is {colored(to_user_info[0], 'light_blue')} {colored(to_user_info[1], 'light_blue')}')

    transfer_confirmation = input(f'Is This right Person({colored('y', 'light_green')}/{colored('n', 'light_red')}): ').lower().strip()
    
    if transfer_confirmation == 'y':
        
        check_if_to_user_card_exsists = check_if_card_exsists(transfer_to_User_ID, transfer_card_type)

        if check_if_to_user_card_exsists:

            from_user_balance = float(get_card_balance(User_ID, transfer_card_type))

            print(f'Balance on Your {transfer_card_type} card: {from_user_balance} USD'.center(20))

            amount_to_transfer_input = input('Please enter amount of money you want to transfer(q): ').lower().strip()

            amount_to_transfer = ''.join(filter(lambda char: char.isdigit(), amount_to_transfer_input))

            if not amount_to_transfer:
                print(colored('Can not transfer this value!', 'red'))
                time.sleep(3)
                User_account(email)

            else:

                if float(amount_to_transfer) > from_user_balance:
                    print(colored('Can not transfer more then you have!', 'red'))
                    time.sleep(3)
                    User_account(email)

                withdraw_on_card(User_ID, transfer_card_type, float(from_user_balance), float(amount_to_transfer))

                to_user_balance = get_card_balance(transfer_to_User_ID, transfer_card_type)

                deposit_on_card(transfer_to_User_ID, transfer_card_type, float(to_user_balance), float(amount_to_transfer))

                print(colored('Successfuly Transfered money!', 'green'))
                time.sleep(3)
                User_account(email)

        else:
            print(colored(f'This User Does not have {transfer_card_type} card!', 'light_red'))
            time.sleep(3)
            User_account(email)

    elif transfer_confirmation == 'n':
        User_account(email)
        
    else:
        print(colored('Not right Answer!', 'light_red'))
        time.sleep(2)
        User_account(email)

def conversion_page(User_ID, email):
    os.system('clear')
    print(colored('*'*100, 'light_green'))
    print(colored('Conversion page'.center(100), 'green'))
    print(colored('*'*100, 'light_green'))
    
    card_type = input('Enter Card Type Here(q): ').strip().lower()

    if card_type == 'q':
        User_account(email)

    while card_type not in ['visa', 'mastercard']:
        card_type = input('Enter Valid Card type Here(q): ').strip().lower()
        if card_type == 'q':
            User_account(email)

    conversion_card_exists = check_if_card_exsists(User_ID, card_type)

    if not conversion_card_exists:
        print(colored('This card is not binded', 'red'))
        time.sleep(3)
        User_account(email)

    conversion_balance = float(get_card_balance(User_ID, card_type))

    print(f'Your {card_type} card balance is {conversion_balance} USD')
 
    cr = CurrencyConverter()
    
    InGEL = round(conversion_balance * 2.81, 2)
    InRUB = round(conversion_balance * 108.78, 2)
    InEURO = round(cr.convert(conversion_balance, 'USD', 'EUR'),2)
    InRupee = round(cr.convert(conversion_balance, 'USD', 'INR'),2)
    InWon = round(cr.convert(conversion_balance, 'USD', 'KRW'),2)
    InYuan  = round(cr.convert(conversion_balance, 'USD', 'CNY'),2)
    InLira  = round(cr.convert(conversion_balance, 'USD', 'TRY'),2)
    InYen  = round(cr.convert(conversion_balance, 'USD', 'JPY'),2)
    InBitcoin = conversion_balance * 0.00001058

    print(f"Balance in GEL (Georgia): {humanize.intcomma(InGEL)}") 
    print(f"Balance in RUB (Russia): {humanize.intcomma(InRUB)}")
    print(f"Balance in Euro (England): {humanize.intcomma(InEURO)}")
    print(f"Balance in Rupee (India): {humanize.intcomma(InRupee)}")
    print(f"Balance in Won (South korea): {humanize.intcomma(InWon)}")
    print(f"Balance in Yuan (China): {humanize.intcomma(InYuan)}")
    print(f"Balance in Yen (Japan): {humanize.intcomma(InYen)}")
    print(f"Balance in Lira (Turkey): {humanize.intcomma(InLira)}")
    print(f"Balance in Bitcoin: {humanize.intcomma(InBitcoin)}")

    conversion_Choice = input('Enter Here Q if you want to return: ').lower()

    while conversion_Choice != 'q':
        conversion_Choice = input('Enter Here Q if you want to return: ').lower()
    
    User_account(email)

if __name__ == '__main__':
    Main_page()
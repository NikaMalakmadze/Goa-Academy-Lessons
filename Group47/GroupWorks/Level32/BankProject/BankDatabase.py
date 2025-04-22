
from BankDatabaseInfo import HOST, USER, PASSWORD, DATABASENAME

import mysql.connector

#ვქმნით ბანკის დატაბეიზის ცვლადს, ვიყენებთ mysql.connector_ს
#დატაბეიზის დასაკავშირებლად საჭირო ინფორმაციას ვღებულობთ BankDatabaseInfo მოდულიდან
BankDatabase= mysql.connector.connect(
    host = HOST,                            #ჰოსტი არის ლოკალური
    user = USER,                            #მომხმარებლის სახელი
    passwd = PASSWORD,                      #დატაბეიზის პაროლი
    database = DATABASENAME                 #დატაბეიზის სახელი, სადაც უნდა ვიმუშაოთ
)

#ვქმნით ეგრედწოდებულ SQLCursor_ს, იგი შეასრულებს ერთგვარი 'სივრცის' როლს სადაც დავწერთ SQL ბრძანებებს
#ვუთითებთ დატაბეიზის ცვლადს და ვიძახებთ მეთოდს cursor
SQLCursor = BankDatabase.cursor()

#ქვემოთ მოცემული არის ფუნქციები, რომლებიც გარკვეულ მხრივ ურთიერთობენ დატაბეიზთან
#   არის ფუნქციები, რომლებიც: 
#           1.იღებენ ინფორმაციას დატაბეიზიდან
#           2.ამოწმებენ არსებობს, თუ არა გარკვეული ინფორმაცია დატაბეიზში
#           3.ამატებენ ინფორმაციას დატაბეიზში
#           4.ცვლიან ინფორმაციას დატაბეიზში

#ფუნქცია, რომელიც იღებს მთლიან სვეტს იმ დათაბეიზიდან, რომელსაც მივუთითებთ და აბრუნებს მას ლისტის(სიის) სახით
#   მას სჭირდება სვეტისა და დატაბეიზის სახელი არგუმენტებად
def get_data_from_database(data, database):

    SQLCursor.execute(f'SELECT {data} FROM {database}')         #ვწერთ ბრძანებას კურსორში

    data = SQLCursor.fetchall()                                 #ვათავსებთ ინფორმაციას ცვლადში

    arr = []                                                    #ვქმნით ცარიელ სიას

    for element in data:                            #დავუაროთ data ცვლადის თითოეულ ელემენტს
        arr.append(element[0])                          #დავამათოთ ელემენტი სიაში

    return arr                                      #დავაბრუნოთ სია

#ფუნქცია, რომელიც ამატებს ახალ მომხმარებელს დატაბეიზში
#   მას არგუმენტად სჭირდება მომხმარებლის პირადი მონაცემები ლისტის(სიის) სახით
def add_user(User_info):

    #ვწერთ SQL ფორმულას სტრინგის სახით და ვათავსებთ ცვლადში
    user_add_formula = 'INSERT INTO accounts (User_ID, name, lastname, Year, mail, password) values(%s,%s,%s,%s,%s,%s)'

    SQLCursor.execute(user_add_formula, User_info)              #ვუშვებთ ბრძანებას

    BankDatabase.commit()                                       #დატაბეიზში ვინახავთ ცვლილებებს

#ფუნქცია, რომელიც ამოწმებს არსებობს, თუ არა მომხმარებელი დატაბეიზში, აბრუნებს bool ტიპის მონაცემებს(True/False)
#   მას არგუმენტად სჭირდება მომხმარებლის იმეილი და პაროლი
def check_if_account_exsits(email, password):

    exsistsformula = f'SELECT COUNT(*) FROM accounts WHERE mail ="{email}" AND password = "{password}"'         #ვწერთ SQL ფორმულას

    SQLCursor.execute(exsistsformula)                                           #ვუშვებთ ბრძანებას

    finded = SQLCursor.fetchone()[0]                                            #ვინახავთ ინფორმაციას ცვლადში

    if finded == 1:                                                 #თუ ცვლადში არის 1
        return True                                                     #ესეიგი მომხმარებელი არსებობს, ვაბრუნებთ True
    
    return False                                                    #სხვა შემთხვევაში, მომხმარებელი არ არსებოსბს, ვაბრუნებთ False

#ფუნქცია, რომელიც დატაბეიზიდან აბრუნებს მომხმარებლის იმ ინფორმაციას, რომელსაც მივუთითებთ მისი იმეილის საშუალებით
#   მას არგუმენტად სჭირდება ინფორმაცია, რომელიც უნდა 'ამოვიღოთ' და მომხმარებლის იმეილი
def get_data_from_user(data, email):

    get_from_user_formula = f'SELECT {data} FROM accounts WHERE mail = "{email}"'           #ვწერთ SQL ფორმულას

    SQLCursor.execute(get_from_user_formula)                                            #ვუშვებთ ბრძანებას

    user_data = SQLCursor.fetchone()[0]                                             #ვინახავთ ინფორმაციას ცვლადში

    return user_data                                                            #ვაბრუნებთ ინფორმაციას

#ფუნქცია, რომელიც აბრუნებს მომხმარებლის ბარათებს და ამ ბარათების ინფორმაციას
#   მას არგუმენტად სჭირდება მომხმარებლის უნიკალური ID 
def get_cards_from_user(user_id):

    get_cards_formula = f'SELECT * FROM cards WHERE User_ID = "{user_id}"'          #ვწერთ ფორმულას

    SQLCursor.execute(get_cards_formula)                                            #ვუშვებთ ბრძანებას

    User_cards = SQLCursor.fetchall()                                       #ვინახავთ ინფორმაციას ცვლადში

    return User_cards                                               #ვაბრუნებთ ინფორმაციას

#ფუნქცია, რომელიც ამატებს მომხმარებლის ბარათს დატაბეიზში
#   მას არგუმენტად სჭირდება ბარათის ინფორმაცია ლისტის(სიის) სახით
def add_card(Card_info):

    card_add_formula = 'INSERT INTO cards (User_ID, card_ID, card_type, balance) values(%s,%s,%s,%s)'       #ვწერთ SQL ფორმულას

    SQLCursor.execute(card_add_formula, Card_info)                                              #ვუშვებთ ბრძანებას

    BankDatabase.commit()                                                               #დატაბეიზში ვინახავთ ცვლილებებს

#ფუნქცია, რომელიც აბრუნებს მომხმარებლის კონკრეტულ ბარათზე ბალანსს
#   მას არგუმენტად სჭირდება მომხმარებლის ID და ბარათის ტიპი
def get_card_balance(user_id, card_type):

    get_card_balance = f'SELECT balance FROM cards WHERE card_type = "{card_type}" AND User_ID = "{user_id}"'   #ვწერთ SQL ფორმულას

    SQLCursor.execute(get_card_balance)                                     #ვუშვებთ ბრძანებას

    cardbalance = SQLCursor.fetchone()[0]                               #ვინახავთ ინფორმაციას ცვლადში

    return cardbalance                                              #ვაბრუნებთ ინფორმაციას

#ფუნქცია, რომელიც ამოწმებს არსებობს, თუ არა მომხმარებლის კონკრეტული ბარათი დატაბეიზში
#   მას არგუმენტად სჭირდება მომხმარებლის ID და ბარათის ტიპი
def check_if_card_exsists(User_ID, card_type):

    SQLCursor.execute(f'SELECT COUNT(*) FROM cards WHERE User_ID = "{User_ID}" AND card_type = "{card_type}"')      #ვწერთ SQL ფორმულას

    finded = SQLCursor.fetchone()[0]                                                                #ვინახავთ შედეგს ცვლადში

    if finded == 1:                                                         #თუ ცვლადში არის 1
        return True                                                             #ესეიგი ბარათი არსებობს, ვაბრუნებთ True

    return False                                                            #სხვა შემთხვევაში, მომხმარებელი არ არსებოსბს, ვაბრუნებთ False

#ფუნქცია, რომელიც 'ადეპოზიტებს' თანხას მომხმარებლის კონკრეტულ ბარათზე
#   მას არგუმენტად სჭირდება მომხმარებლის ID, ბარათის ტიპი, ამჟამინდელი ბალანსი, და თანხის ოდენობა, რომელიც უნდა 'დავადეპოზიტოთ'
def deposit_on_card(User_ID, card_type, balance, amount):

    #ვწერთ SQL ფორმულას
    Deposit_Formula = f'UPDATE cards SET balance = {balance + amount} WHERE User_ID = "{User_ID}" AND card_type = "{card_type}"'

    SQLCursor.execute(Deposit_Formula)                          #ვუშვებთ ბრძანებას

    BankDatabase.commit()                                       #დატაბეიზში ვინახავთ ცვლილებებს

#ფუნქცია, რომელიც 'ჭრის' თანხას მომხმარებლის კონკრეტულ ბარათზე
#   მას არგუმენტად სჭირდება მომხმარებლის ID, ბარათის ტიპი, ამჟამინდელი ბალანსი, და თანხის ოდენობა, რომელიც უნდა 'ჩამოვჭრათ'
def withdraw_on_card(User_ID, card_type, balance, amount):

    #ვწერთ SQL ფორმულას
    Withdraw_Formula = f'UPDATE cards SET balance = {balance - amount} WHERE User_ID = "{User_ID}" AND card_type = "{card_type}"'

    SQLCursor.execute(Withdraw_Formula)                                 #ვუშვებთ ბრძანებას

    BankDatabase.commit()                                               #დატაბეიზში ვინახავთ ცვლილებებს

#ფუნქცია, რომელიც აბრუნებს მომხმარებლის სახელსა და გვარს კორტეჟის(Tuple) სახით
#   მას არგუმენტად სჭირდება მომხმარებლის ID
def get_info_from_user(User_ID):

    User_Info_Formula = f'SELECT name, lastname FROM accounts WHERE User_ID = "{User_ID}"'          #ვწერთ SQL ფორმულას

    SQLCursor.execute(User_Info_Formula)                                            #ვუშვებთ ბრძანებას

    User_info = SQLCursor.fetchall()[0]                                             #ვინახავთ ინფორმაციას ცვლადში
    
    return User_info                                                            #ვაბრუნებთ ინფორმაციას

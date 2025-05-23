
import os
import time

# გააკეთეთ shooping card ის კალათა, მომხმარებელის დახმარებით შეავსეთ კალათა და შექმენით dict ი, მომხარებელს უნდა შეეძლოს ახალი პროდუქტების დამატება თავისი ფასით, შეეძლება რომელიმე კონკრეტულის ამოშლა, კოდი არშეწყვეტს მუშაობას მანამ სანამ მომხმარებელი ამას არ მოისურვებს, მომხმარებელს უნდა შეეძლოს იმ ყველაფრის გაკეთება რა მეთოდებიც გვაქვს, უნდა შეეძლოს პროდუქტის რედაქტირება, ფასის რედაქტირება

products = {}

def add_product():
    global products
    name = input('Enter Product name: ')
    price = input('Enter Product price: ')

    if not price.isdigit():
        raise ValueError('Invalid Price format! ')

    products[name] = price

def edit_product():
    global products
    name = input('Enter Product name: ')

    if name not in products:
        print('No Such Product!')
        time.sleep(1)
        return
    
    price = input('Enter Product price: ')

    products[name] = price

def delete_product():
    global products
    name = input('Enter Product name: ')

    if name not in products:
        print('No Such Product!')
        time.sleep(1)
        return

    del products[name]

    print(f'Deleted Product: {name}')

    time.sleep(1)

while True:

    print('Welcome To Admin Panel!')
    print('1. add Product')
    print('2. edit Product')
    print('3. delete Product')
    print('4. save and quit')

    answr = input('Please Input your answer: ').strip().lower()

    if answr == '1':
        add_product()
    elif answr == '2':
        edit_product()
    elif answr == '3':
        delete_product()
    elif answr == '4':
        break
    else:
        print('Invalid Input!')
            
    os.system('clear')
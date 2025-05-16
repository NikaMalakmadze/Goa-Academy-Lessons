
# task 1

def add_user():
    name = input('Enter Account name: ')
    lastname = input('Enter Account lastName: ')

    mail = input('Enter Account mail: ')
    if '@' not in mail:
        return 'Invalid mailformat'
    
    password = input('Enter Account PassWord: ')

    user = {
        'user_name': name,
        'user_lastName': lastname,
        'user_mail': mail,
        'user_password': password
    }

    return user

accounts = []

while True:

    answr = input('add account(y if yes): ').strip().lower()

    if answr != 'y':
        break
            
    accounts.append(add_user())

# task 2

person = {
    'name': 'Diana Johnson',
    'age': '34',
    'city': 'Berlin',
    'id': '4729'
}

for key in person.keys():
    print(f'key: {key} | value: {person[key]}')

# task 3

# შექმენით dict ამ დიქტში შეინახეთ რაღაც ინფორმაციები, შექმენით დამატებითი სია ელემენტებით და შემდეგ დიქტის თითოეული კის მნიშველობა ჩაანავლეთ სიის ელემენტებით, შექმენით მეორე დიქტი სადაც მზგავს ინფორმაციას შეინახავთ და ამ დიქტის მნიშვნელობებს ჩაანაცვლებთ პირველი დიქტის საწყისი მნიშვნელობებით

person1 = {
    'name': 'Charlie Brown',
    'age': 42,
    'city': 'Tokyo',
    'id': 3187
}

person2 = {
    'name': 'Eve Smith',
    'age': 29,
    'city': 'Paris',
    'id': 6852
}

_list = ['banana', 'orange', 'grape', 'kiwi']

for key in person2.keys():
    person2[key] = person1[key]

# ორი ვარიანი
for index, key in enumerate(person1.keys()):
    person1[key] = _list[index]

index = 0
for key in person1.keys():
    person1[key] = _list[index]
    index += 1

print(person1)
print(person2)
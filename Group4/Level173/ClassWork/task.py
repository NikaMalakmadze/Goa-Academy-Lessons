
# 1) შექმენით სია ან ტუპლი ამ სიაში გქონდეთ შენახული რიცხვები გამოიყენეთ map ფუნქცია და დაბეჭდეთ ახალი სია სადაც იქნება წინა სიიდან გაორმაგებული ელემენტები

def mult(n): return  n * 2

my_list = [1, 2, 3, 4, 5, 6, 7]

new_list = list(map(mult, my_list))

print(new_list)

# 2) შექმენით სია ან ტუპლი ამ სიაში გქონდეთ შენახული რიცხვები, შექმენით მზგავსი მეორე სია სხვადასხვა რიცხვებით, გამოიყენეთ map ფუნქცია და დაბეჭდეთ ახალი სია სადაც იქნება მოცემული ორი სიიდან თანმიმდევრულად ელემენტების ერთმანეთზე ნამრავლი

def items_mult(n1, n2): return  n1 * n2

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

new_list = list(map(items_mult, list1, list2))

print(new_list)


# 3) # შექმენით სია ან ტუპლი ამ სიაში გქონდეთ შენახული რაიმე სიმბოლოები(!@#$), შექმენით მზგავსი მეორე სია რომელშიც გექნებათ სახელები(სტრინგები) გამოიყენეთ map ფუნქცია და lambda რომლითაც შეიქმნება ახალი სია სადაც იქნება ელემენტი ასე პრინციპით: სიმბოლო-სახელი => #name, @surname

symbols = ["!", "@", "#", "$"]
names = ['name1', 'name2', 'name3', 'name4']

combined = list(map(
    lambda symbol, name: symbol+name, 
    symbols, 
    names
))

print(combined)

# 4) შექმენით სია სადაც შეინახავთ მომხმსარებლების ასაკს, შემდეგ კი filter ფუნქციის გამოყენებით გაფილტრეთ და შექმენით ამ სიისგან ახალი სია ისე რომ ახალ გაფილტრულ სიაში იყოს მხოლოდ სრლუწლოვნები

ages = [34, 56, 23, 6, 4, 97, 8, 2, 70, 18]

valid_ages = list(filter(lambda age: age >= 18, ages))

print(valid_ages)

# 5) შექმენით მომხარებლის სახელბეით სავსე სია შემდეგ კი filter ის და lambda ს დახმარებით დააბრუნეთ ახალი სია სადაც იქნება მხოლოდ ისეთი სახელები რომლებიც იწება a ასოზე

names = ['akaki', 'sandro', 'Andria', 'gela']

a_names = list(filter(lambda name: name[0] in 'aA', names))

print(a_names)

# 6) შექმენით ფუნქცია რომელსაც შეეძლება მიიღოს უსასრულო რაოდენობით არგუმენტი, შემდეგ კი მიღებული არგუმენტებისგან დააბრუნეთ ახალი სია სადაც თითოეულ არგუმენტ დაუმატებთ სიტყვას "-#_#-"

names1 = ['dato', 'nika', 'Lasha', 'giorgi']
names2 = ['zura', 'vakho', 'Tornike', 'levani']
names3 = ['irakli', 'beka', 'Misho', 'temuri']

chained_names = list(map(
    lambda *args: ["-#_#-"+ name for name in args],
    names1,
    names2,
    names3,
))

print(chained_names)


# task 1 

file = open('Group4/Level174/ClassWork/test.txt', 'r')

print(file.read())

file.close()

# 1) შექმენით ტექსტური ფაილი, წაიკითხეთ ეს ფაილი შემდეგ კი დაბეჭდეთ 4 ხაზის პირველი 5 სიმბოლო ფაილის დახურვა არდაგავიწყდეთ

file = open('Group4/Level174/ClassWork/test.txt', 'r')

print(file.readlines()[3][:5])

file.close()

# 2) ტექსტურ ფაილში სათითაოდ ხაზებზე დაწერეთ სხვადასხვა რიცხვები შემდეგ ეს ფაილი წაიკითხეთ შექმენით ორი სია ერთი ლუწი რიცხვებისთვის მეორე კენტებისთვის და წაკითხული მონაცემებიდან გაანაწილეთ შესაბამის სიაში ელემენტები

evens, odds = [], []

with open('Group4/Level174/ClassWork/test.txt', 'r') as f:
    for line in f:
        line = line.strip()

        try:
            floated = float(line)
        except (TypeError, ValueError):
            print(f'Skipped line with {line}')
            continue

        evens.append(floated) if floated % 2 == 0 else odds.append(floated)
        
print(evens)
print(odds)

# 3) შექმენით ფაილი შემდეგ გახსენით ეს ფაილი ისე რომ შეძლოთ ტექსტის გადაწერა, გადააწერეთ ზემოდან რაიმე ტექსტი და ჩაამატეთ დამატებით ტექსტი

try:
    with open('Group4/Level174/ClassWork/test1.txt', 'x'):
        print('Created!')
except FileExistsError:
    print('Already Exists!')

with open('Group4/Level174/ClassWork/test1.txt', 'w') as f:
    f.write('Edited!')

with open('Group4/Level174/ClassWork/test1.txt', 'a') as f:
    f.write('Modified!')
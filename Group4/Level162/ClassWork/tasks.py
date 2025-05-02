
# Working With Tuples 

names = ("name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8", "name9", "name10")

for i in range(1, len(names), 2):
    print(names[i])

middle_three = names[len(names)//2 - 1 : len(names)//2 + 2]

print(f'Middle three items: {middle_three}')

print(f'Tuple length: {len(names)}')

#task 1

def manual_difference(set1, set2):
    return set([i for i in set1 if i not in set2])

set1 = {1, 2, 3, 4, 5}

set2 = {1, 2, 4}

print(manual_difference(set1, set2))

#task 2

student1 = {
    'name': 'zurabi',
    'surname': 'romanadze',
    'age': '15',
    'score': '10'
}

student2 = {
    'name': 'nodari',
    'surname': 'fartenadze',
    'age': '16',
    'score': '8'
}

print(student1.items())
print(student2.items())
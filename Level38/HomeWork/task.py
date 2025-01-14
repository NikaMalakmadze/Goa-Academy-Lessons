
#task 1

print("-------------TASK-1-------------")

setOne = {1, 2, 3, 4, 5}

setTwo = {1, 2, 4, 6, 7, 8}

setThree = {10, 20, 30}

setFour = {34, 56, 78}

#1. add element to set
setOne.add(54)
print(f'1. {setOne}')

#get copy of the set
setOneCopy = setOne.copy()
print(f'2. {setOneCopy}')

#difference of this set and another set
print(f'3. {setOne.difference(setTwo)}')

#remove element from set but if element is not in set it gives error
setOne.remove(54)
print(f'4. {setOne}')

#remove element from set but if element is not in set it does not gives error
print(f'5. {'No Errors' if not setOne.discard(65) else 1}')      # 65 is not in setOne, no errors

#get intersection of sets as a new set
print(f'6. {setOne.intersection(setTwo)}')

#returns True if two sets has not intersection else False
print(f'7. {setOne.isdisjoint(setThree)}')

#Test whether every element in the set is in other.
print(f'8. {setOne.issubset(setTwo)}')

#Test whether every element in other is in the set.
print(f'9. {setOneCopy.issuperset(setOne)}')

#all elements that are in exactly one of the sets.
print(f'10. {setOne.symmetric_difference(setTwo)}')

#get intersection of two sets and update first set with that intersection
setOne.intersection_update(setOneCopy)
print(f'11. {setOne}')

#get difference of two sets and update first set with that difference
setOne.difference_update(setTwo)
print(f'12. {setOne}')

#get all elements that are in exactly one of the sets and update first that with that elements.
setOneCopy.symmetric_difference_update(setThree)
print(f'13. {setOneCopy}')

#updates the first set, by adding elements from another set
setThree.update(setTwo)
print(f'14. {setThree}')

#remove random element from set
print(f'15. {setOne.pop()}')

#clear set, remove all elements
setOne.clear()
print(f'16. {setOne}')

#union of two sets, all elements that are in either set
print(f'17. {setFour.union(setTwo)}')

#task 2

print("-------------TASK-2-------------")

MyDict = {
    'name': 'Nika',
    'lastname': 'Malakmadze',
    'age': 16,
}

print(*MyDict.keys(), sep= ', ')

#task 3

print("-------------TASK-3-------------")

print(*MyDict.values(), sep= ', ')

#task 4

print("-------------TASK-4-------------")

database = {}

def add_to_database(database, name, lastname, age):
    for title, info in zip(['name', 'lastname', 'age'], [name, lastname, age]):
        database[title] = info

add_to_database(database, 'nika', 'malakmadze', '16')

print(database)
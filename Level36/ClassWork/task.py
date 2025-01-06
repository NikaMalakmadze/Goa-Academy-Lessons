
#task 1

def digitize(n):
    return [int(i) for i in str(n)[::-1]]

print(digitize(4346))

#task 2

def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

print(is_anagram("foefet", "toffee"))

#task 3

def get_count(sentence):
    return len([i for i in sentence if i in 'aeiou'])

print(get_count('feaegaew'))

#task 4

def filter_list(l):
    return [i for i in l if type(i) == int]

print(filter_list([1, 2, 'a', 'b']))

#task 1

def digitize(n):
    return [int(i) for i in str(n)[::-1]]

print(digitize(4346))

#task 2

def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

print(is_anagram("foefet", "toffee"))
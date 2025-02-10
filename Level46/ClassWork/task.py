
# task 1

def filter_list(l):
    return [i for i in l if type(i) == int]

print(filter_list([1, 'a', 'b', 0, 15]))

# task 2

def disemvowel(string_):
    return ''.join(i for i in string_ if i not in "aeiouAEIOU")

print(disemvowel("This website is for losers LOL!"))

# task 3

def descending_order(num):
    str_ = sorted(str(num)[:], reverse=True)
    return int(''.join(str_))

print(descending_order(635747))
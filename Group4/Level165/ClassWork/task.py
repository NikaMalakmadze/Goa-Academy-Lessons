
# 1 დაწერე ფუნქცია, რომელიც იღებს tuple-ს და აბრუნებს მის სიგრძეს. 

def tuple_len(tp):
    return len(tp)

# 2 მოცემულია t = (10, 20, 30, 40, 50) დაბეჭდე მეორე და ბოლო ელემენტი.

t = (10, 20, 30, 40, 50)

print(t[1], t[-1])

# 3 შექმენი ორი tuple და გააერთიანე ისინი ახალად.

t1 = (10, 20)
t2 = (30, 40, 50)

t_union = t1+t2

# 4 დუბლიკატების დათვლა დაწერე ფუნქცია, რომელიც ითვლის რამდენჯერ მეორდება კონკრეტული ელემენტი tuple-ში.

def count_tuple_element(tp, value):
    return tp.count(value)

print(count_tuple_element(t_union, 10))

# 5 გადაეცემა რიცხვების tuple — დააბრუნე ახალი tuple, რომელიც დალაგებულია ზრდადობით

def sorted_tuple(tp):
    return tuple(sorted(tp))

unsorted_tuple = (3, 5053, 31, 53, 64, 352, 1, 36, 365)

print(sorted_tuple(unsorted_tuple))

# 6 ჩაანაცვლე tuple-ში არსებული ყველა 0 ელემენტი None-ით და დააბრუნე ახალი tuple.

def replace_zeros(tp):
    arr = []
    for i in tp:
        arr.append(None) if i == 0 else arr.append(i)
    return tuple(arr)

print(replace_zeros((1, 35, 53, 0, 15, 0, 68, 0, 0, 45, 4, 1, 0)))

# განმეორებადი ელემენტების მოცილება tuple-დან დაწერე ფუნქცია, რომელიც იღებს tuple-ს და აბრუნებს ახალ tuple-ს განმეორებითი ელემენტების გარეშე (პირველი ინახება).

def remove_dublicates(tp):
    return tuple(set(tp))

tuple_with_dublicates = (10, 10, 30, 50, 50, 30, 13, 50, 34, 56, 34)

print(remove_dublicates(tuple_with_dublicates))

# sets

a = {1, 2, 3, 4, 1}
b = {3, 4, 5, 6}

union = a | b
print(union)

intersection = a & b
print(intersection)

diff_a = a - b
print(diff_a)

diff_b = b - a
print(diff_b)

# დაწერე ფუნქცია, რომელიც შეამოწმებს, არის თუ არა ერთი set მეორის subset ან superset

def check_sets(_set1, _set2):
    if _set1.issubset(_set2) or _set1.issuperset(_set2): return True
    return False

print(check_sets(a, b))

# უნიკალური სიტყვების ამოღება ტექსტიდან გადაეცემა ტექსტი. დააბრუნე ყველა უნიკალური სიტყვა (set-ის სახით).

def unique_words(_str):
    words_original = set(_str.split())
    words = _str.split()
    for word in words:
        if words.count(word) >= 2:
            words[words.index(word)] = word + '|'
    
    words = set(words)

    unique_words = words - words_original

    arr = []

    for word in unique_words:
        arr.append(word[:-1])

    return words_original - set(arr)

def unique_words_v2(_str):
    words = _str.split()
    _set = set()
    for word in words:
        if words.count(word) == 1:
            _set.add(word)
    return _set

text = "He walked into the room. it was filled with the silence."

print(unique_words(text))
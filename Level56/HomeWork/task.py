
# task 1

print("-------------TASK-1-------------")

def solution(text, ending):
    return text.endswith(ending)

print(solution("samurai", "ai"))

# task 2

print("-------------TASK-2-------------")

def even_or_odd(s):
    e = 0
    o = 0
    for i in s:
        if int(i)%2==0:
            e += int(i)
        else:
            o += int(i)
    if e == o: return 'Even and Odd are the same'
    if e > o: return 'Even is greater than Odd'
    return 'Odd is greater than Even'

print(even_or_odd('123'))

# task 3

print("-------------TASK-3-------------")

def even_numbers(arr,n):
    return [i for i in arr if i % 2 == 0 ][-n:]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# task 4

print("-------------TASK-4-------------")

def vowel_indices(word):
	return [i for i, v in enumerate(word, 1) if v in 'aeiouyAEIOUY']

print(vowel_indices("UNDISARMED"))

# task 5

print("-------------TASK-5-------------")

def geometric_sequence_elements(a, r, n):
    last = a
    arr = [last]
    while len(arr) != n:
        last *= r
        arr.append(last)
    return ', '.join(map(str, arr))

print(geometric_sequence_elements(2, 2, 10))

# task 1

def double_char(s):
    return "".join(i*2 for i in s)

print(double_char('String'))

# task 2

def get_age(age):
    return int(age[0])

print(get_age('2 years old'))

# task 3

def feast(b,d):
    return b[0]==d[0] and b[-1]==d[-1]

print(feast("great blue heron", "garlic naan"))

# task 4

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

print(array_plus_array([1, 2, 3], [4, 5, 6]))

# task 5

def solution(n):
    return sum(i for i in range(3, n) if i%3 == 0 or i%5 == 0)
  
print(solution(15))
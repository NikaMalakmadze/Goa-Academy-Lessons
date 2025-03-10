
# task 1

def angle(n):
    return (n-2)*180

print(angle(5))

# task 2

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_triangle(1, 2, 3))

# task 3

def solution(nums):
    return [] if not nums else sorted(nums)

print(solution([1,2,3,10,5]))
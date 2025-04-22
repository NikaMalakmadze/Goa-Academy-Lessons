
#task 1

print("-------------TASK-1-------------")

chars = ["a","b","c","d","e","g","e","i","w","r","o","q","a","u"]

vowels = "aeiou"

count = 0

for i in range(len(chars)):
    if chars[i] in vowels:
        count += 1

print(count)

#task 2

print("-------------TASK-2-------------")

nums = [11,23,45,65,76,87,15,30,34,66,87,98,75,90,105,14,46]

for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print(num)

#task 3

print("-------------TASK-3-------------")

arr = ["13",154,"av","g","45",34,0.54,"gbr","fehuehf",86,576,"3fae","fegr"]

result = ""

for i in range(len(arr)):
    result += str(arr[i])

print(result)

#task 4

print("-------------TASK-4-------------")

size = int(input("Enter size:"))

for i in range(1, size):
    print(i * " " + size * "*")

#task 5

print("-------------TASK-5-------------")

age = int(input("Are you 12y old? | Enter your age: "))

if age > 12:
    print("You are not 12y old")
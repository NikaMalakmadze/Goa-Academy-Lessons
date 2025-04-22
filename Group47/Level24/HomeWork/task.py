
#task 1

print("-------------TASK-1-------------")

arr = []

temp = ""

str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

for i in range(len(str)):

    if str[i] != " ":
        temp += str[i]

        if i == len(str) - 1:
            arr.append(temp)

    else:
        arr.append(temp)
        temp = ""

print(arr)

#task 2

print("-------------TASK-2-------------")

joined = ""

for i in arr:
    joined += i + " "

print(joined)

#task 3

print("-------------TASK-3-------------")

txt = "lorem ipsum"

replaced_txt = ""

for i in txt:
    if i == "m":
        replaced_txt += "n"
    else:
        replaced_txt += i

print(replaced_txt)

#task 4

print("-------------TASK-4-------------")

num1 = float(input("Please enter first num: "))
num2 = float(input("Please enter Second num: "))

operation = input("Please enter Mathematical operation(+,-,*,/): ")

if operation == "+":
    print(f"answer: {num1 + num2}")

elif operation == "-":
    print(f"answer: {num1 - num2}")

elif operation == "*":
    print(f"answer: {num1 * num2}")

elif operation == "/":
    print(f"answer: {num1 / num2}") if num2 != 0 else print(f"Can't Divide {num1} on {num2}!")

else:
    print("Please input valid mathematical operations!")

#task 5

print("-------------TASK-5-------------")

word = ""

count = 1

array = []

print("Type _Q_ to Quit: ")

while word != "_Q_":
    word = input(f"Please enter {count} word: ")

    if word != "_Q_":
        array.append(word)

    count += 1

joined_array = " ".join(array)

print(joined_array)
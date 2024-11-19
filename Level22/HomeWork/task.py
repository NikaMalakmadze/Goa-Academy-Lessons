
#task 1

print("-------------TASK-1-------------")

list_of_names = ["nika", "davit", "giorgi", "saba","sandro","nika","luka"]

print(list_of_names.count("nika"))

#task 2

print("-------------TASK-2-------------")

nums = [4, 4, 65, 76,34, 54, 45, 2, 43, 5, 68, 45, 2,89, 57, 78]

nums.reverse()

print(nums)

#task 3

print("-------------TASK-3-------------")

list_of_numbers = [1, 2, 3]

list_lenght = len(list_of_numbers)

list_of_numbers = list_of_numbers * list_lenght

print(list_of_numbers)

#task 4

print("-------------TASK-4-------------")

insert_arr = ["python", "c#", "rust", "c++", "javascript", "java"]

insert_arr.insert(1 , "davit")

print(insert_arr)

#task 5

print("-------------TASK-5-------------")

names_list = ["nika", "davit", "giorgi", "saba","sandro","nika","luka"]

print(names_list.count("nika"))

while "nika" in names_list:
    names_list.remove("nika")

print(len(names_list), names_list)
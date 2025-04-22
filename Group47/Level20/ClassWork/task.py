
#task 1

nums = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(nums)):
    if nums[i] % 2 == 1:
        nums[i] = "odd"

for num in nums:
    print(num , "" , end="")

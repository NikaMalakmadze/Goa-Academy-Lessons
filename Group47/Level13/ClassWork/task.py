
#task 1

name = "Two Tower"
result = ""

####result  უნდა მიიღოს name  ის მნიშნველოაბ ოღონდ ისე უნდა ვქნათ, რომ სათითაოდ უნდა დამეატოს საიტერაციო ცვლადები ( i )

for i in name:
    result += i

print(result)

#task 2

num = int(input("Please enter number: "))

print("KENTI") if num % 2 == 1 else print("AR ARIS KENTI, ES RICXVI ARIS LUWI")


#task 3

for i in range(1, 100):
    if i % 2 == 0:
        print(i , "luwi")
    else:
        print(i , "kenti")

# task 1

def rot13(message):
    letters = ['abcdefghijklmABCDEFGHIJKLM', 'nopqrstuvwxyzNOPQRSTUVWXYZ']
    res = ""
    for i in message:
        if i in letters[0]:
            index = letters[0].index(i)
            res += letters[1][index]
        elif i in letters[1]:
            index = letters[1].index(i)
            res += letters[0][index]
        else:
            res += i
    return res
        
print(rot13('Hello World'))
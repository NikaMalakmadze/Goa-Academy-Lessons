
#task 1

def lowes_and_highest(strn):
    arr = [int(i) for i in strn.split()]
    return f"{min(arr)} {max(arr)}"
    
print(lowes_and_highest("1 2 3 4 10"))
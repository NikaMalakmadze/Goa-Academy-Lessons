
# task 1

def is_isogram(string):
    return False if[i for i in string if string.lower().count(i) >= 2] else True

print(is_isogram('feagueha'))

# task 2

def accum(st):
    res = ''
    for i in range(len(st)):
        res += st[i].upper() + st[i].lower() * i
        if i != len(st)-1:
            res += '-'
    return res

print(accum('feageg'))
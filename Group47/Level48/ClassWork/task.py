
# task 1

def xo(s):
    return s.lower().count('x') == s.lower().count('o')

print(xo('oxoxx'))

# task 2

def find_short(s):
    return min([len(l) for l in s.split()])

print(find_short("bitcoin take over the world maybe who knows perhaps"))

# task 3

def solution(text, ending):
    return text.endswith(ending)

print(solution("sumo", "omo"))

# task 4

def accum(st):
    res = ''
    for i in range(len(st)):
        res += st[i].upper() + st[i].lower() * i
        if i != len(st)-1:
            res += '-'
    return res

print(accum("ZpglnRxqenU"))
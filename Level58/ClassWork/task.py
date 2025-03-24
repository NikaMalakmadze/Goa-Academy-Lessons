
# task 1

def lottery(s):
    r = ''
    for i in s:
        if i.isdigit() and i not in r:
            r += i
    return r if r else "One more run!"

print(lottery('geaet3253'))

# task 2

def longest_word(str_):
    d = {len(w):w for w in str_.split()}
    return d[max(d.keys())]

print(longest_word('forward each step going'))
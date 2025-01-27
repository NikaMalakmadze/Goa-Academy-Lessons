
# task 1

def points(games):
    score = 0
    for i in games:
        if int(i[0])>int(i[2]):
            score += 3
        elif int(i[0])==int(i[2]):
            score += 1
    return score

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))

# task 2

def toBinary(num):
    if num == 0:
        return 0
    output = ''
    while num > 1:
        output += str(num%2)
        num = num // 2
    output += '1'
    return output[::-1]

print(toBinary(16))

# task 3

def fake_bin(x):
    return ''.join("0" if i < "5" else "1" for i in x)

print(fake_bin('3526246'))

# task 4

def dna_to_rna(dna):
    return dna.replace('T', 'U')

print(dna_to_rna('TTTT'))
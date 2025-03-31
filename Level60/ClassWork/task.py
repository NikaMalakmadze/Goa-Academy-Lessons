
# task 1

def count_arara(n):
    adakC = n // 2
    if n%2 == 0: return ' '.join(['adak'] * adakC)
    return ' '.join(['adak'] * adakC + ['anane'])

print(count_arara(9))

# task 2

def is_planet_mnemonic_correct(solar_system, mnemonic):
    solarW = [i[0] for i in solar_system if i[0] != 'A']
    mnemonicW = [i[0] for i in mnemonic.split()]
    return mnemonicW == solarW

print(is_planet_mnemonic_correct(["Mercury", "Asteroid", "Saturn"], "My Shoes"))

# task 3

def max_possible_score(points, seen): 
    return sum([v*2 if k in seen else v for k, v in points.items()])

print(max_possible_score({"a": 1}, []))
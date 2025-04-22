
# task 1

def count_by(x, n):
    return [x * i for i in range(1, n + 1)]

print(count_by(2, 10))

# task 2

def get_planet_name(id):
    dict = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return dict[id]

print(get_planet_name(3))

# task 3

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years, 15, 15]
    if human_years == 2:
        return [human_years, 24, 24]
    else:
        return [human_years, 24 + ((human_years - 2) * 4), 24 + ((human_years - 2) * 5)]
    
print(human_years_cat_years_dog_years(53))

# task 4

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old*2))

print(twice_as_old(55,30))

# task 5

def greet(language):
    data = [ ("english", "Welcome")
            , ("czech", "Vitejte")
            , ("danish", "Velkomst")
            , ("dutch", "Welkom")
            , ("estonian", "Tere tulemast")
            , ("finnish", "Tervetuloa")
            , ("flemish", "Welgekomen")
            , ("french", "Bienvenue")
            , ("german", "Willkommen")
            , ("irish", "Failte")
            , ("italian", "Benvenuto")
            , ("latvian", "Gaidits")
            , ("lithuanian", "Laukiamas")
            , ("polish", "Witamy")
            , ("spanish", "Bienvenido")
            , ("swedish", "Valkommen")
            , ("welsh", "Croeso")
            ]
    for lang in data:
        if language == lang[0]:
            return lang[1]
    return data[0][1]

print(greet('english'))

# task 1

# task solved using List Comprehension :)

def even_or_odd(n):
    return 'Even' if int(''.join(i for i in str(n))) % 2 == 0 else 'Odd'

print(even_or_odd(474))
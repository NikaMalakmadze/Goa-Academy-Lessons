
# შექმენით სია რომელშიც იქნება რაღაც სახელები შენახული ამის შემდეგ list comprehension ის გამოყენებით დაბეჭდეთ სია სადაც იქნება პირველი სიიდან მხოლოდ ის ელემენტები როლმებიც არ შეიცავენ a ასოს

names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

not_a_names = [name for name in names if 'a' not in name.lower()]

print(not_a_names)
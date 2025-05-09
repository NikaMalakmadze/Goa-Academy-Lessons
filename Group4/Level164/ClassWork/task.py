
# task 1

'''
    შექმენით სეტი სადაც გექნებათ მინიმუმ 10 ელემენტი შემდეგ დაბეჭდეთ მხოლოდ ის ელემენტები რომლებიც იწყება a ასოზე, ჩაამატეთ დამატებით რამდენიმე ახალი ელემენტი, შემდეგ გადაუარეთ მთელ სეტს და ამოშალეთ სეტიდან ისეთი ელემენტები რომლებიც იწყება b ასოზე, ამის შემდეგ შექმენით მეორე ახალი სეტი სადაც გექნებათ რამდენიმე ელემენტი გადაუარეთ ამ სეტს და პირველ სეტში დაამატეთ მხოლოდ ისეთი ელემენტები რომლებიც იწყება g ასოზე ხოლო დამატებით შექმენით მესამე სეტი და გააერთიანეთ უკვე შეცვლილ და განახლებულ პირველ სეტთან და ამ გაერთიენების მერე ხელახლა შეასრულეთ ის ყველაფერი რაც მაღლა იყო
'''

def get_word_by_letter(_set, letter):
    _output = set()
    for word in _set:
        if word[0] == letter:
            _output.add(word)

    return _output

def subtask(set_one):
    # 3
    b_words = get_word_by_letter(set_one, 'b')

    return set_one - b_words

def task(set_one, set_two, set_three):

    # 1
    print(*get_word_by_letter(set_one, 'a'))

    # 2
    set_one.add("bed")
    set_one.add("bat")
    set_one.add("robot")

    set_one = subtask(set_one)

    # 4
    g_words = get_word_by_letter(set_two, 'g')

    set_one.update(g_words)

    # 5
    set_one.update(set_three)

    set_one = subtask(set_one)

    return set_one

set_one = {"apple", "chair", "dog", "book", "ant", "tree", "android", "water", "sun", "fish"}
set_two = {"frog", "cup", "bag", "leaf", "hat", 'guy', 'girl', 'bbbbbbbbb'}
set_three = {"lamp", "rock", "sock", "door", "map", 'ball', 'bbbbbbbb'}

set_one = task(set_one, set_two, set_three)

print(set_one)

set_two = {"apple", "orange", "banana", "grape", "pear", "dog", "cat"}
set_three = {"chair", "table", "bed", "sofa", "shelf"}

set_one = task(set_one, set_two, set_three)

print(set_one)
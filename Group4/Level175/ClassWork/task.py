
# 1) შექმენი ტექსტური ფაილი  და დაბეჭდე სულ რამდენი სიტყვაა ამ ფაილში, ასევე რამდენი უნიკალური სიტყვაა, ასევე ყველაზე ხშირი სიტყვა

from itertools import zip_longest

data: dict = {
    'total_words': 0,
    'unique_words': [],
    'popular_word': ''
}

def get_file_info() -> None:
    words: list = []
    words_counts: dict = {}

    with open('Group4/Level175/ClassWork/text.txt', 'r') as f:
        for line in f:
            words.append(line.strip())

    for word in words:
        words_counts[words.count(word)] = word

    most_count: int = max(words_counts.keys())

    data['total_words'] = len(words)
    data['unique_words'] = set(words)
    data['popular_word'] = words_counts[most_count]

def order_words() -> None:
    words: list = []
    with open('Group4/Level175/ClassWork/names.txt', 'r') as f:
        for line in f:
            words.append(line.strip())

    def get_first() -> str:
        first: str = words[0]
        for word in words:
            if word < first:
                first = word
        words.remove(first)
        return first
    
    sorted_words = []
    for _ in range(len(words)):
        sorted_words.append(get_first())

    with open('Group4/Level175/ClassWork/names.txt', 'w') as file:
        file.write('\n'.join(sorted_words))

get_file_info()
order_words()

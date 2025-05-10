
from datetime import datetime
import json
import time
import os

# constant variables where are stored paths to the needed files
NEW_WORDS_FILE = ''                                             # path to words txt file
OUTPUT_FILE = ''                                                # path to progress json file

# helper/utility class that is validating user input and working with files
class LoadFile:
    ''' 
        Class That is working with loading files and validating inputs

        Methods

        | __init__ |
        constructor, gets paths to the txt and json files, validates paths and loads data from them

        | valid_words_file |
        static method that checks if 'words_file' argument is in correct format + checks if actual txt file exsists

        | valid_progress_file |
        static method that checks if 'default_output_path' argument is in correct format + creates json file if it doesn't exsists

        | load_words |
        static method that loads data(words) from the txt file

        | load_progress |
        method that opens json file and gets data from it

    '''

    def __init__(self, words_file, default_output_path):
        if self.valid_words_file(words_file) and self.valid_progress_file(default_output_path):
            self.default_output_path = default_output_path
            self.progress_info = self.load_progress()
            self.input_words = self.load_words(words_file)

    @staticmethod
    def valid_words_file(words_file):
        if isinstance(words_file, str) and os.path.exists(words_file) and words_file.endswith('.txt'):
            return True
        raise ValueError('Incorrect word input format or non exsisting File!')
    
    @staticmethod
    def valid_progress_file(default_output_path):
        if isinstance(default_output_path, str) and default_output_path.endswith('.json'):
            if not os.path.exists(default_output_path):
                with open(default_output_path, 'w') as f:
                    pass
            return True
        raise ValueError('Incorrect default output file format!')

    @staticmethod
    def load_words(words_file):
        with open(words_file, 'r') as words:
            return set(word.strip().lower() for word in words)
        
    def load_progress(self):
        try:

            with open(self.default_output_path, 'r') as f:
                data = json.load(f)
                total_words = set(data.get('total_words', []))
                learned_words = set(data.get('learned_words', []))
                inProgress_words = set(data.get('inProgress_words', []))
                notLearned_words = set(data.get('notLearned_words', []))
                new_words = set(data.get('new_words', []))

            return {
                'total_words': total_words,
                'learned_words': learned_words,
                'inProgress_words': inProgress_words,
                'notLearned_words': notLearned_words,
                'new_words': new_words
            }
        
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Progress json File is empty. You are new here :)")
            return {
                'total_words': set(),
                'learned_words': set(), 
                'inProgress_words': set(),
                'notLearned_words': set(),
                'new_words': set()
            }

# Vocabulary class that tracks words   
class Vocabulary(LoadFile):
    '''
        Class that does main features of this program. it extends LoadFile Class

        Methods 

        | __init__ |
        constructor, calls parent class and validates input. saves different data from the json file as an object attributes
        calls 'update_progress' method

        | update_progress | 
        method that finds out new words from the inputed txt file + updates 'not_learned_words' set

        | remove_word |
        method that can temporarily remove word from all "categories" or remove it from vocabulary permanently 

        | output_progress |
        method that combines all data together and saves it in the json file

    '''

    def __init__(self, words_file, default_output_path):
        super().__init__(words_file, default_output_path)
        self.total_words = self.input_words | self.progress_info['total_words']
        self.learned_words = self.progress_info['learned_words']
        self.in_progress_words = self.progress_info['inProgress_words']
        self.new_words = self.progress_info['new_words'] 
        self.not_learned_words = self.progress_info['notLearned_words'] | self.input_words
        self.update_progress()

    def update_progress(self, update_new=True):
        if update_new:

            progress = self.progress_info

            for new_word in progress['new_words']:
                self.not_learned_words.add(new_word)
        
            progress['new_words'].clear()

            for word in self.input_words: 
                if word not in progress['learned_words'] and word not in progress['inProgress_words'] and word not in progress['notLearned_words']:
                    self.new_words.add(word)

        self.not_learned_words = self.total_words - self.learned_words - self.in_progress_words

    def remove_word(self, word, remove_from_all=False):
        if remove_from_all:
            self.total_words.discard(word)
            self.new_words.discard(word)
            return
        self.learned_words.discard(word)
        self.in_progress_words.discard(word)
        self.not_learned_words.discard(word)

    def output_progress(self):
        output_info = {
            'stats': {
                'last_edited': datetime.now().strftime(r'%Y-%m-%d %H:%M:%S'),
                "total_words": len(self.total_words),
                "learned": len(self.learned_words),
                "in_progress": len(self.in_progress_words),
                "not_learned": len(self.not_learned_words),
                "new_words": len(self.new_words)
            },
            'total_words': sorted(list(self.total_words)),
            'learned_words': sorted(list(self.learned_words)), 
            'inProgress_words': sorted(list(self.in_progress_words)),
            'notLearned_words': sorted(list(self.not_learned_words)),
            'new_words': sorted(list(self.new_words))
        }

        with open(self.default_output_path, 'w') as f:
            json.dump(output_info, f, indent=3)

# main fucntion that has a user interface role in this program 
def main():
    # create Vocabulary object
    vocab = Vocabulary(NEW_WORDS_FILE, OUTPUT_FILE)

    while True:

        # print current stats
        print('---------Statistics---------')
        print(f"  Total Words      : {len(vocab.total_words)}")
        print(f"  Learned          : {len(vocab.learned_words)}")
        print(f"  In Progress      : {len(vocab.in_progress_words)}")
        print(f"  Not Learned      : {len(vocab.not_learned_words)}")
        print(f"  New Words        : {len(vocab.new_words)}")

        # ask user to enter word
        word = input("\nEnter a word you've studied (or type 'exit' to quit): ").strip().lower()

        # save progress and break if user typed exit
        if word == 'exit':
            vocab.output_progress()
            print('Progress Saved!')
            break

        # if word not in vocabulary, ask if she/he wants to add it
        if word not in vocab.total_words:
            answer = input("Word not in vocabulary list. Would You like to add it? (y if yes): ").strip().lower()
            if answer == 'y':
                vocab.total_words.add(word)
                vocab.new_words.add(word)
                print('Word added to the vocabulary!')
                time.sleep(1)
            os.system('clear')
            continue

        # ask user what she/he wants to do with it
        print("Mark as (l)earned, (p)racticing, or (r)emove from vocabulary: ")
        action = input().strip().lower()

        # temporarily remove word from all "categories"
        vocab.remove_word(word)

        # depended on user input add word in to the correct category, or remove it from vocabulary
        if action == 'l':
            vocab.learned_words.add(word)
            print("Marked as learned.")
        elif action == 'p':
            vocab.in_progress_words.add(word)
            print("Marked as in progress.")
        elif action == 'r':
            vocab.remove_word(word, True)
            print("Removed from tracking.")
        else:
            print("Invalid action.")

        # update 'not_learned_words' set
        vocab.update_progress(False)

        # clear terminal
        os.system('clear')

if __name__ == '__task__':
    main()
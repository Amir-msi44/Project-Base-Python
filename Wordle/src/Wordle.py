import random
from collections import Counter

from utils import print_error, print_success, print_warning

random.seed(42)


class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10000):
       self.word_len = word_len
       self.words = self.generate_word_frequency(file_path, word_len, limit)

    def generate_word_frequency(self, file_path: str, word_len: int, limit: int):
        # Build Data
        words = []
        with open(file_path) as f:
            for line in f:
                word, frequency = line.split(', ')
                words.append((word, int(frequency)))

        # Filter Data
        words = list(filter(lambda w: len(w[0]) == word_len, words))

        # Sort Data
        words = sorted(words, key=lambda w: w[1], reverse=True)

        # Limit
        words = words[:limit]

        #Drop Frequency
        words = [w[0] for w in words]

        return words

    def run(self,):
        word = random.choice(self.words).upper()
        num_try = 6
        word_counter = Counter(word)

        while num_try:
            guess_word = input(f'Please enter a {self.word_len} letter word (or q to exit)').upper()
            if guess_word == 'Q':
                break

            # Word lenght
            if len(guess_word) != self.word_len:
                print(f'Word is not a {self.word_len} letter word. You entered {len(guess_word)}!')
                continue

            #Validity Check
            if guess_word.lower() not in self.words:
                print_warning('Word is not valid')
                continue

            guess_counter = Counter()
            output = [' _ '] * self.word_len  # Placeholder for output

            # First pass with zip: checking for correct letters in correct positions
            for i, (w_letter, g_letter) in enumerate(zip(word, guess_word)):
                if w_letter == g_letter:
                    print_success(f' {g_letter} ', end=' ')
                    guess_counter[g_letter] += 1
                    output[i] = g_letter
                else:
                    print(' _ ', end=' ')  # Placeholder for the second pass
            print()

            # Second pass: check for correct letters in wrong positions
            for i, g_letter in enumerate(guess_word):
                if output[i] == ' _ ':  # Only process if not already found in the correct position
                    if g_letter in word and guess_counter[g_letter] < word_counter[g_letter]:
                        print_warning(f' {g_letter} ', end=' ')
                        guess_counter[g_letter] += 1
                    else:
                        print_error(f' {g_letter} ', end=' ')
            print()


            if word == guess_word:
                print()
                print_success('Congrats!')
                break

            num_try -= 1
            if num_try == 0:
                print(f'You Lost!\nCorrect Answer is {word}')

if __name__ == '__main__':
    wordle = Wordle(file_path)
    Wordle.run()

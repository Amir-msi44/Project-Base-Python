from Wordle import Wordle

file_path = "data/words_frequency.txt"
if __name__ == '__main__':
    wordle = Wordle(file_path)
    wordle.run()
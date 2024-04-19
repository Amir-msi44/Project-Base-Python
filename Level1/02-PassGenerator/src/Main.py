import random
import string
from abc import ABC, abstractmethod
import nltk


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPassGenerator(PasswordGenerator):
    def __init__(self, length, include_numbers=False, include_symbols=False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePassGenerator(PasswordGenerator):
    def __init__(
        self,
        num_of_words: int,
        capitalize: bool = False,
        separator_type: str = '-',
        vocabulary: list = None
    ):
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()

        self.num_of_words = num_of_words
        self.capitalize = capitalize
        self.separator = separator_type

    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]

        return self.separator.join(password_words)


if __name__ == '__main__':
    p_obj = RandomPassGenerator(10)
    print(p_obj.generate())

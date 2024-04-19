import string
from abc import ABC, abstractmethod

from termcolor import colored


class TextProcessor(ABC):
    @abstractmethod
    def transform(self, text):
        pass


class ConvertCase(TextProcessor):
    def __init__(self, casing='lower'):
        self.casing = casing

    def transform(self, text):
        if self.casing == 'lower':
            return text.lower()
        elif self.casing == 'upper':
            return text.upper()
        elif self.casing == 'title':
            return text.title()


class RemoveDigit(TextProcessor):
    def transform(self, text):
        return ''.join(char if not char.isdigit() else ' ' for char in text)


class RemoveSpace(TextProcessor):
    def transform(self, text):
        return ' '.join(text.split())


class RemovePunkt(TextProcessor):
    def transform(self, text):
        return ''.join(char if not char in string.punctuation else ' ' for char in text)


class TextPipeline:
    def __init__(self, *args):
        self.transformers = args

    def transform(self, text):
        for i in self.transformers:
            text = i.transform(text)
        return text

    def __str__(self):
        transformers = ' -> '.join([tf.__class__.__name__ for tf in self.transformers])
        return f'Pipeline: [{transformers}]'

def print_success(text):
    print(colored(text, 'green'))
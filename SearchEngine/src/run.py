from collections import Counter
from pathlib import Path

from utils import (ConvertCase, RemoveDigit, RemovePunkt, RemoveSpace,
                   TextPipeline, print_success)


class Search:
    def __init__(self, document_path, stopwords_path):
        self.data = self.crawl(document_path)
        self.pipe = TextPipeline(ConvertCase(), RemoveDigit(), RemovePunkt(), RemoveSpace())
        self.stopwords = self.read_stopwords(stopwords_path)
        self.index = self.PerformIndex()

    def crawl(self, document_path):
        data = {}
        for doc_path in Path(document_path).iterdir():

            if doc_path.suffix != '.txt':
                continue

            with open(doc_path) as f:
                doc_name = doc_path.stem.replace('_',' ').title()
                data[doc_name] = f.read()

        return data

    def read_stopwords(self, stopwords_path):
        with open(stopwords_path) as file:
            stop_words = file.readlines()
        stop_words = [self.pipe.transform(word.strip()) for word in stop_words]
        return stop_words

    def PerformIndex(self,):
        index = {}
        for doc_name, content in self.data.items():
            for word in content.split():
                word = self.pipe.transform(word)

                # Empty Words
                if not word:
                    continue

                # Ignore Stop Words
                if word in self.stopwords:
                    continue

                # Add to index
                if index.get(word):
                    index[word].add(doc_name)
                else:
                    index[word] = {doc_name, }
        return index

    def search(self, search_input):
        TOP_N = 3
        search_input = self.pipe.transform(search_input)
        # Get input tokens
        search_tokens = search_input.split()

        # Get relevant documents
        docs = []
        for token in search_tokens:
            docs.extend(self.index.get(token, []))

        # Rank documents
        docs_counter = Counter(docs).most_common()
        docs = [d[0] for d in docs_counter][:TOP_N]

        return docs

if __name__ == '__main__':
    searcher = Search('src/data/documents', 'src/data/stop_words.txt')

    while True:
        # Get user input
        search_input = input('Search to find a doc (q to quit):')
        if search_input.lower() == 'q':
            break
        docs = searcher.search(search_input)
        # Print the results
        for doc in docs:
            print_success(f'- {doc}')
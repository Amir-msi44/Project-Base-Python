import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

class WordCloudGen:

    def __init__(self, filepath):
        with open(filepath) as f:
            self.text = f.read().split('\n')

    def run(self, output):
        self.text = ' '.join(self.text)
        wordcloud = WordCloud(background_color='White').generate(self.text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        wordcloud.to_file(output)

if __name__ == '__main__':
    wc_gen = WordCloudGen('src/data/movies.txt')
    wc_gen.run('output.png')

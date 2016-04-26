"""


class SearchEnglish(SearchLanguage):
    lang = 'en'
    js_stemmer_code = js_porter_stemmer
    stopwords = english_stopwords

    def init(self, options):
        if CSTEMMER:
            class Stemmer(CStemmer):
                def stem(self, word):
                    return self(word.lower())
        else:
            class Stemmer(PorterStemmer):
                """All those porter stemmer implementations look hideous;
                make at least the stem method nicer.
                """
                def stem(self, word):
                    word = word.lower()
                    return PorterStemmer.stem(self, word, 0, len(word) - 1)

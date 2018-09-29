# Natural Language Toolkit: code_stemmer_indexing
import nltk
from nltk.corpus import wordnet as wn

class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4)                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay, rdisplay)
            semantic_index = wn.synsets(i)[0].offset

    def _stem(self, word):
        return self._stemmer.stem(word).lower()

def concordance_extended(word, stemmer, text, width=40):
    key = stemmer.stem(word).lower()
    wc = int(width/4) # words of context
    nltk.Index((stemmer.stem(word).lower(), i) for (i, word) in enumerate(text))
    for i in self._index[key]:
        lcontext = ' '.join(text[i-wc:i])
        rcontext = ' '.join(text[i:i+wc])
        ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
        rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
        print(ldisplay, rdisplay)
        semantic_index = wn.synsets(i)[0].offset    


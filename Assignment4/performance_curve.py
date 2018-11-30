import nltk
from nltk.corpus import brown
from random import shuffle

def unigram_performance(cfd, set_size):
    brown_tagged_sents = brown.tagged_sents(categories='news')
    unigram_tagger = nltk.UnigramTagger(brown_tagged_sents[:set_size])
    return unigram_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    set_sizes = list(range(10, len(brown.sents(categories='news')), 10))
    perfs = [unigram_performance(cfd, size) for size in set_sizes]
    pylab.plot(set_sizes, perfs, '-bo')

    pylab.title('Lookup Tagger Performance with Varying Training Set Size')
    pylab.xlabel('Training Set Size')
    pylab.ylabel('Performance')
    pylab.show()

display()
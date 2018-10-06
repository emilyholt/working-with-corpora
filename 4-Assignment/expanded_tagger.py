import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import brown

def sorted_tags():
    '''
    Produce an alphabetically sorted list of the distinct words tagged as MD. 
    '''
    tagged_words = nltk.corpus.brown.tagged_words()
    words_of_interest = []
    for tag_pair in tagged_words:
        if tag_pair[1] == 'MD':
            words_of_interest.append(tag_pair[0].lower())
    distinct_words_of_interest = list(set(words_of_interest))
    distinct_sorted_words_of_interest = sorted(distinct_words_of_interest, key=str.lower)

    print("Distinct words tagged as MD: %s" % distinct_sorted_words_of_interest)
    print("Number of distinct_words_of_interest: %s" % len(distinct_sorted_words_of_interest))

def multi_tags():
    brown_tagged = brown.tagged_words()
    data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_tagged)
    words_of_interest = []
    for word in sorted(data.conditions()):
        if len(data[word]) > 2:
            tags = [tag for (tag, _) in data[word].most_common()]
            if ('VBZ' in tags and 'NNS' in tags):
                # print(word, ' '.join(tags))
                words_of_interest.append(word)
    print("Words categorized as both VBZ and NNS: ")
    print(words_of_interest)

def find_phrase():
    for tagged_sent in brown.tagged_sents():
        for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(tagged_sent):
            if (t1=='IN' and t2 == 'DT' and t3=='NN'):
            # if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
                print(w1, w2, w3)
                # print((w1,t1), (w2,t2), (w3,t3))

if __name__ == '__main__':
    find_phrase()



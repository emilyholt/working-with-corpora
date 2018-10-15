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
            if (t1=='IN' and t2 == 'AT' and t3=='NN'):
                print(w1, w2, w3)

def gendered_tags():
    tagged_words = nltk.corpus.brown.tagged_words(tagset='universal')
    masculine_pronouns = ['his', 'hisself',  'him','hymselfe', 'he', 'himself',"'im",'himselfe', 'hym']
    feminine_pronouns = ['herself', 'her','hers','she',]

    masculine_instances = 0
    feminine_instances = 0

    for tag_pair in tagged_words:
        if tag_pair[1] == 'PRON':
            if tag_pair[0].lower() in masculine_pronouns:
                masculine_instances += 1
            if tag_pair[0].lower() in feminine_pronouns:
                feminine_instances += 1

    print("Masculine pronouns: %s" % masculine_instances)
    print("Feminine pronouns: %s" % feminine_instances)
    print("Ratio: %s" % (masculine_instances / feminine_instances))



if __name__ == '__main__':
    gendered_tags()



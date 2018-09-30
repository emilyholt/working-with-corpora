'''
Readability measures are used to score the reading difficulty of a text, 
for the purposes of selecting texts of appropriate difficulty for language learners. 
Let us define μw to be the average number of letters per word, and μs to be the 
average number of words per sentence, in a given text. 

The Automated Readability Index (ARI) of the text is defined to be: 
4.71 μw + 0.5 μs - 21.43
Compute the ARI score for various sections of the Brown Corpus, 
including section f (lore) and j (learned). Make use of the fact that 
nltk.corpus.brown.words() produces a sequence of words, while 
nltk.corpus.brown.sents() produces a sequence of sentences.
'''

import nltk
import sys
from nltk.corpus import brown

def readability(input):
	letters = brown.raw(categories=input)
	words = brown.words(categories=input)
	sentences = brown.sents(categories=input)
	
	letters_per_word = len(letters) / len(words)
	words_per_sentence = len(words) / len(sentences)
	
	ari_score = (4.71 * float(letters_per_word)) + (0.5 * float(words_per_sentence)) - 21.43
	print("Letters per word: %s" % letters_per_word)
	print("Words per sentence: %s" % words_per_sentence)
	print("ARI Score: %s" % ari_score)
	

if __name__ == '__main__':
	readability(sys.argv[1])
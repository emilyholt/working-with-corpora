from __future__ import division
import sys
import nltk
from nltk.book import *
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer

def sponsor_occurrences(words):
	num_sponsor_occurr = 0
	for word in words:
		if word.lower() == "sponsor" or word.lower() == "sponsored":
			num_sponsor_occurr += 1
	return num_sponsor_occurr

def ad_occurrences(words):
	num_ad_occurr = 0
	for word in words:
		if word.lower() == "ad":
			num_ad_occurr += 1
	return num_ad_occurr

def vocab_size(words):
	return len(set(words))

def lexical_diversity(words): 
	set_len = len(set(words))
	text_len = len(words)
	return float(set_len) / float(text_len)

def frequency_distribution(tokens):
	fdist = FreqDist(tokens)
	return fdist.most_common(100)

def extract_pronouns(words):
	tagged_content = pos_tag(words.split())
	propernouns = [word for word,pos in tagged_content if pos == 'NNP'] 
	print(propernouns)
	return propernouns

def main(args):
	filename = args[1]
	text = []
	with open(filename) as f:
		text = f.readlines()

	words = []
	for line in text:
		for word in line.split():
			words.append(word)

	string = ""
	with open(filename, 'r') as f:
		string=f.read().replace('\n', '').lower()

	print("Corpus size: %d" % len(words))
	print("Vocab size: %d" % vocab_size(words))
	print("Lexical diversity: %0.4f" % lexical_diversity(words))
	print("Number of sponsor occurrences: %d" % sponsor_occurrences(words))
	print("Number of ad occurrences: %d" % ad_occurrences(words))
	tokens = nltk.tokenize.word_tokenize(string.lower())
	# tokenizer = RegexpTokenizer(r'\w+')
	# tokens = tokenizer.tokenize(words)
	print("Frequency Distribution: %s" % frequency_distribution(tokens))
	# propernouns = extract_pronouns(words)

if __name__ == "__main__":
	main(sys.argv)


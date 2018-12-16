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
	tagged_content = pos_tag(words)
	propernouns = [word for word,pos in tagged_content if pos == 'NNP'] 
	return propernouns

def pronoun_frequency(pronouns, string):
	pronoun_frequency_dict = {}
	for noun in set(pronouns):
		noun_count = string.count(str(noun + " "))
		pronoun_frequency_dict[noun] = noun_count
		if noun_count >= 10:
			print("High frequency noun: %s; Count: %d" % (noun, noun_count))
	return pronoun_frequency_dict

def product_frequency(words, string):
	string = string.lower()
	products = ["jeans", "denim", "pants", "dress", "skirt", "shirt", "top", "bottoms", "bag", "scarf", "sunglasses", "shoes", "sneakers", "flats", "heels", "boots", "coat", "jacket", "sweater", "accessories"]
	product_frequency_dict = {key: 0 for key in products}
	for word in words:
		if word in products:
			product_count = string.count(word.lower())
			product_frequency_dict[word] = product_count

	for key in product_frequency_dict:
		print("%s count: %d" % (key, product_frequency_dict[key]))
	return product_frequency_dict
	

	product_counts = []
	for product in products:
		product_counts.append(product_frequency_dict[product])

	print("Product frequencies: ")
	print(product_counts)


def analyze_content(args):
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
		string=f.read().replace('\n', '')

	print("Corpus size: %d" % len(words))
	print("Vocab size: %d" % vocab_size(words))
	print("Lexical diversity: %0.4f" % lexical_diversity(words))
	print("Number of sponsor occurrences: %d" % sponsor_occurrences(words))
	print("Number of ad occurrences: %d" % ad_occurrences(words))
	
	tokens = nltk.tokenize.word_tokenize(string.lower())
	print("Frequency Distribution: %s" % frequency_distribution(tokens))
	pronouns = extract_pronouns(words)
	print("Song of Style High Frequency Pronouns")
	pronoun_frequency_dict = pronoun_frequency(pronouns, string)
	print_most_frequent_pronouns(pronoun_frequency_dict)
	print("Pronoun frequency: %s" % pronoun_frequency(pronouns, string))

	product_frequency_dict = product_frequency(words, string)

if __name__ == "__main__":
	analyze_content(sys.argv)


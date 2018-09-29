import bs4
from bs4 import BeautifulSoup
from urllib import request, response
import nltk
import re
import ssl
import sys

def stem(word):
	for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
		if word.endswith(suffix):
			return word[:-len(suffix)]
	return word

def calc_unknown(url):
	ssl._create_default_https_context = ssl._create_unverified_context
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html).get_text()
	tokens = re.findall(r'\b[a-z]+\b', raw)
	# token_stems = re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', raw)
	known_words = [w for w in nltk.corpus.words.words('en') if w.islower()]
	unknown = list(set(tokens).difference(set(known_words)))

	token_stems = [stem(w) for w in tokens]
	unknown_stems = list(set(token_stems).difference(set(known_words)))


	print("Unknown word stems: %s" % unknown_stems)
	print("Length of raw response: %d" % len(raw))
	print("Number of unknown words in of raw response: %d" % len(set(unknown)))
	print("Number of unknown word stems in of raw response: %d" % len(set(unknown_stems)))
	

if __name__ == '__main__':
	calc_unknown(sys.argv[1])
from urllib import request, response
import nltk
import re
import ssl
import sys

def calc_unknown(url):
	ssl._create_default_https_context = ssl._create_unverified_context
	response = request.urlopen(url)
	raw = response.read().decode('utf8')
	tokens = re.findall(r'/\b[a-z]+\b/', raw)
	print(tokens)
	known_words = [w for w in nltk.corpus.words.words('en') if w.islower()]
	unknown = list(set(tokens).difference(set(known_words)))

	print("Unknown words: %s" % unknown)
	print("Length of raw response: %d" % len(raw))
	print("Number of unknown words in of raw response: %d" % len(set(unknown)))
	

if __name__ == '__main__':
	calc_unknown(sys.argv[1])
import nltk
from nltk import FreqDist
from collections import Counter

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

def calculate_freq_dist():
	male_words = read_words("male_lines.txt")
	female_words = read_words("female_lines.txt")

	male_most_common = Counter(male_words).most_common(70)
	female_most_common = Counter(female_words).most_common(70)

	male_most_common = male_most_common[20:]
	female_most_common = female_most_common[20:]

	print("Most common words in male speeches: %s" % male_most_common)
	print("\n========================================\n" )
	print("Most common words in female speeches: %s" % female_most_common)

	print("\n========================================\n" )
	

if __name__ == '__main__':
	calculate_freq_dist()
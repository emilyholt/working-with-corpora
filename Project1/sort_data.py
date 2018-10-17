import argparse
import os
import pickle
import sys

import numpy as np

#loop over text -> if line = male, start at next line and add to speaking point until next male/female
# HARDCODING MALE == 0, FEMALE == 1
''' 
TODO
1. Turn characters => male vs female
2. combine all texts into one file
3. create new file with no male vs female
4. For each word => replace with number (using lookup table? using genism/Dan's models?)
'''

def create_lookup_tables(text):
    """
    Create lookup tables for vocabulary
    :param text: The text of tv scripts split into words
    :return: A tuple of dicts (vocab_to_int, int_to_vocab)
    """
    index = 1
    vocab_to_int = {}
    int_to_vocab = {}
    
    for word in text:
        if word not in vocab_to_int:
            vocab_to_int[word] = index
            int_to_vocab[index] = word
            index += 1
    
    return (vocab_to_int, int_to_vocab)

def token_lookup():
    """
    Generate a dict to turn punctuation into a token.
    :return: Tokenize dictionary where the key is the punctuation and the value is the token
    """
    # TODO: Implement Function
    token_dict = {}
    token_dict["."] = "||period||"
    token_dict[","] = "||comma||"
    token_dict["\""] = "||quotation_mark||"
    token_dict["\'"] = "||single_quote||"
    token_dict[";"] = "||semicolon||"
    token_dict["!"] = "||exclamation_mark||"
    token_dict["?"] = "||question_mark||"
    token_dict["("] = "||left_parentheses||"
    token_dict[")"] = "||right_parentheses||"
    token_dict["--"] = "||dash||"
    token_dict["\n"] = "||return||"
    
    return token_dict

def load_data(path):
    """
    Load Dataset from File
    """
    input_file = os.path.join(path)
    with open(input_file, "r") as f:
        data = f.read()

    return data

# Load in raw_text_data and return lookup table
def preprocess_and_save_data(raw_dataset_path, token_lookup, create_lookup_tables):
    """
    Preprocess Text Data
    """
    text = load_data(raw_dataset_path)

    token_dict = token_lookup()
    for key, token in token_dict.items():
        text = text.replace(key, ' {} '.format(token))

    text = text.lower()
    text = text.split()

    return create_lookup_tables(text)
    # pickle.dump((int_text, vocab_to_int, int_to_vocab, token_dict), open('preprocess.p', 'wb'))

def preprocess_gendered_data(gendered_dataset_path, token_lookup):
    """
    Preprocess Text Data
    """
    text = load_data(gendered_dataset_path)

    token_dict = token_lookup()
    for key, token in token_dict.items():
        text = text.replace(key, ' {} '.format(token))

    return text

def load_preprocess():
    """
    Load the Preprocessed Training data and return them in batches of <batch_size> or less
    """
    return pickle.load(open('preprocess.p', mode='rb'))

def split_text(gendered_dataset_path, raw_dataset_path):
	vocab_to_int, int_to_vocab = preprocess_and_save_data(raw_dataset_path, token_lookup, create_lookup_tables)
	gendered_text = open(gendered_dataset_path, "r")
	
	speeches = []
	labels = []
	speaking_point = []
	for line in gendered_text:
		if line == 'MALE\n':
			labels.append(0)
			speeches.append(speaking_point)
			speaking_point = []
		elif line == 'FEMALE\n':
			labels.append(1)
			speeches.append(speaking_point)
			speaking_point = []
		else:
			line = line.lower()
			for word in line.split():
				int_text = vocab_to_int[word] 
				speaking_point.append(int_text)
	
	# Write the last line, since we dont loop again
	speeches.append(speaking_point)
	# Get rid of the first, since that was empty
	speeches = speeches[1:]
	# Save the dataset in a pickle file we can load later
	pickle.dump((labels, speeches), open('preprocess.p', 'wb'))

	print(labels)
	print(speeches)
	print("Label len: %s" % len(labels))
	print("Speeches len: %s" % len(speeches))

def test():

	labels, speeches = pickle.load(open('preprocess.p', mode='rb'))
	print("Pickle-loaded Label len: %s" % len(labels))
	print("Pickle-loaded Speeches len: %s" % len(speeches))


if __name__ == '__main__':
	# split_text("gendered_shrew_test.txt", "shrew_test.txt")
	split_text("gendered_data.txt", "raw_text_data.txt")
	test()


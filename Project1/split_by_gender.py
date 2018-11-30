import argparse
import os
import pickle
import sys

import numpy as np

def split_text(input_text):
	# vocab_to_int, int_to_vocab = preprocess_and_save_data(raw_dataset_path, token_lookup, create_lookup_tables)
	gendered_text = open(input_text, "r")
	
	male_lines = open("male_lines.txt", "w")
	female_lines = open("female_lines.txt", "w")

	male_speaking_points = []
	female_speaking_points = []
	speaking_point = []
	most_recent_gender = "MALE"

	for line in gendered_text:
		if line == 'MALE\n':
			# if len(speaking_point) != 0:
			# 	male_speaking_points.append(speaking_point)
			# 	speaking_point = []
			most_recent_gender = "MALE"
		elif line == 'FEMALE\n':
			# if len(speaking_point) != 0:
			# 	female_speaking_points.append(speaking_point)
			# 	speaking_point = []
			most_recent_gender = "FEMALE"
		else:
			line = line.lower()
			if most_recent_gender == "MALE":
				male_lines.write(line)
			else:
				female_lines.write(line)
				
	# Write the last line, since we dont loop again

	male_lines.close()
	female_lines.close()
	gendered_text.close()

if __name__ == '__main__':
	split_text(sys.argv[1])
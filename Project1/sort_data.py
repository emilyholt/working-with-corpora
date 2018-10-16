import argparse
import sys

#loop over text -> if line = male, start at next line and add to speaking point until next male/female
# HARDCODING MALE == 0, FEMALE == 1
''' 
TODO
1. Turn characters => male vs female
2. combine all texts into one file
3. create new file with no male vs female
4. For each word => replace with number (using lookup table? using genism/Dan's models?)
'''


def split_text(play):
	print("Opening %s ..." % play)
	text = open(play)
	speeches = []
	labels = []
	speaking_point = ''
	for line in text:
		if line == 'MALE\n':
			labels.append([0])
			speeches.append([speaking_point])
			speaking_point = ''
		elif line == 'FEMALE\n':
			labels.append([1])
			speeches.append([speaking_point])
			speaking_point = ''
		else:
			speaking_point += line.rstrip('\n')
	speeches.append(speaking_point)

	speeches = speeches[1:]
	print(labels)
	print(speeches)
	print("Label len: %s" % len(labels))
	print("Speeches len: %s" % len(speeches))

if __name__ == '__main__':
	split_text(sys.argv[1])


import argparse
import nltk 
import numpy 
import pylab
import random

def zipf_law_plot(input_text, title):
    fdist = nltk.FreqDist(input_text)
    pylab.plot(range(fdist.B()), fdist.values())
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.title(title)
    pylab.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--random', action='store_true', help="Generate random text")
    parser.add_argument('-i', '--input', type=str, help="Zipf plot of input text")
    args = parser.parse_args()

    if not args.random and not args.input:
        print("Error: must pass in an argument")
        return

    if args.random:
        target_length = 808080

        random_string = ""
        while len(random_string) < target_length:
            random_string += random.choice('abcdefg ')
            
        # Tokenize random string and generate the Zipf plot
        random_text = random_string.split()
        print("Plot of Zipf's Law for random text")
        zipf_law_plot(random_text, "Zipf Plot for Random Text")

    if args.input:
        zipf_law_plot(random_text, "Zipf Plot for %s Text" % args.input)

    
if __name__ == "__main__":
    main()

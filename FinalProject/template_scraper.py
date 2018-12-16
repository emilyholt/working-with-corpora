from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import sys

# CONFIGURABLE VARIABLES
#-----------------------#
# Key words like "Comments" or "Notify me" that you do not want in your corpus
REPETITIVE_PHRASES = ()

# Typically starts with both "http:" and "https:", and any other important offshoots
BASE_URLS = ()

# URLS to Instagram, Facebook, Pinterest, or other frequent links
# that you do not want to explore and include in the corpus
UNIMPORTANT_URLS = ()

OUTPUT_FILE = "new_blog_content.txt"
#-----------------------#


def get_new_links(url):
	data = requests.get(url)
	content = data.text
	soup = BeautifulSoup(content, 'html.parser')
	links_of_interest = set()
	for link in soup.find_all('a'):		
		new_link = str(link.get('href'))
		if (new_link.startswith(BASE_URLS) and not new_link.startswith(BASE_URLS)) and new_link.endswith("/"):
			links_of_interest.add(new_link)

	return links_of_interest

def get_paragraphs(url):
	'''
	Returns available urls for visible pictures
	'''

	data = requests.get(url)
	content = data.text

	soup = BeautifulSoup(content, 'html.parser')
	blog_paragraphs = []
	for paragraph in soup.find_all('p'):		
		text = str(paragraph.text)
		if not text.startswith(REPETITIVE_KEYWORDS):
			blog_paragraphs.append(text)

	return blog_paragraphs

def get_all_links(base_link):
	links_already_explored = []

	links_to_explore = set(get_new_links(base_link))
	while len(links_to_explore) != 0:
		link = links_to_explore.pop()
		if link not in links_already_explored:
			links_already_explored.append(link)
			links_to_explore.update(get_new_links(link))
	return links_already_explored

def get_all_content(links_list):
	f = open(OUTPUT_FILE, 'a') 
	for link in links_list:
		content = get_paragraphs(link)
		for component in content:
			f.write(component)
			f.write("\n\n")
	f.close()


if __name__ == '__main__':
 	# Get all unique links from the blog
	all_links = get_all_links(sys.argv[1])
	# Scrape the content from each of the links
	get_all_content(all_links)

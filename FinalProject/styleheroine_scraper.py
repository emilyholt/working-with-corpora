from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import sys

def get_styleheroine_links(url):
	data = requests.get(url)
	content = data.text
	# print(content)
	soup = BeautifulSoup(content, 'html.parser')
	links_of_interest = set()
	# print(soup.find_all('a'))
	for link in soup.find_all('a'):		
		new_link = str(link.get('href'))
		if (new_link.startswith("http://www.styleheroine.com/") or new_link.startswith("https://www.styleheroine.com")) and new_link.endswith("/"):
			# print("Link found: %s" % new_link)
			links_of_interest.add(new_link)
	# print("Links of interest")
	# print(links_of_interest)
	return links_of_interest

def get_styleheroine_paragraphs(url):
	'''
	Returns available urls for visible pictures
	'''

	data = requests.get(url)
	content = data.text

	soup = BeautifulSoup(content, 'html.parser')
	blog_paragraphs = []
	for paragraph in soup.find_all('p'):		
		text = str(paragraph.text)
		if not text.startswith("Our weekly newsletter") and not text.startswith("View the editorial") and not text.startswith("Notify me") and not text.startswith("Styleheroine.com consists of"):
			# print(text)
			blog_paragraphs.append(text)

	return blog_paragraphs

def scrape_styleheroine(url):
	f = open("styleheroine_content.txt", 'a')
	new_links = get_styleheroine_links(url)
	for link in new_links:
		content = get_styleheroine_paragraphs(link)
		for component in content:
			f.write(component)
			f.write("\n\n")
	f.close()
	print("Complete!")



if __name__ == '__main__':
	for i in range(1, 100):
		print("Processing Page # %d" % i)
		url = str(sys.argv[1]) + "/page/" + str(i)
		scrape_styleheroine(url)

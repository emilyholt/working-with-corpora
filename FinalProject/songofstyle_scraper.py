from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import sys

def get_content(url):
	data = requests.get(url)
	content = data.text
	print(content)

def get_songofstyle_links(url):
	data = requests.get(url)
	content = data.text

	soup = BeautifulSoup(content, 'html.parser')
	links_of_interest = set()
	for link in soup.find_all('a'):		
		new_link = str(link.get('href'))
		if (new_link.startswith("http://www.songofstyle.com") or new_link.startswith("https://www.songofstyle.com")) and new_link.endswith(".html"):
			links_of_interest.add(new_link)
	return links_of_interest

def get_songofstyle_paragraphs(url):
	'''
	Returns available urls for visible pictures
	'''
	blog_content = []
	data = requests.get(url)
	content = data.text
	article_body_pattern = re.compile("\"articleBody\": \"(.*?)\"")
	blog_paragraphs = article_body_pattern.findall(content)
	# print(blog_paragraphs)
	return blog_paragraphs

def scrape_songofstyle(url):
	f = open("songofstyle_content.txt", 'a')
	new_links = get_songofstyle_links(url)
	for link in new_links:
		content = get_songofstyle_paragraphs(link)[0]
		f.write(content)
		f.write("\n\n")
	f.close()
	print("Complete!")



if __name__ == '__main__':
	for i in range(1, 381):
		print("Processing Page # %d" % i)
		url = str(sys.argv[1]) + "/page/" + str(i)
		scrape_songofstyle(url)
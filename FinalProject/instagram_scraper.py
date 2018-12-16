from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import sys

def get_content(url):
	data = requests.get(url)
	content = data.text
	print(content)


def parse_base_urls(url):
	'''
	Returns available urls for visible pictures
	'''
	data = requests.get(url)
	content = data.text
	shortcode_pattern = re.compile("\"shortcode\":\"(.*?)\"")
	base_urls = shortcode_pattern.findall(content)
	urls = [url + "p/" + link for link in base_urls]

	return urls

def get_location(url):
	data = requests.get(url)
	content = data.text

	location_pattern = re.compile("\"location\":{(.*?)}")
	location_tags = location_pattern.findall(content)
	print(location_tags)
	return location_tags


def return_caption(url):
	data = requests.get(url)
	content = data.text
	soup = BeautifulSoup(content, features="html.parser")
	caption = str(soup.title)
	caption = caption.strip("<title>\n")
	caption = caption.strip("</title>")
	caption = caption.split(":", 1)[1]

	return caption

def wheel(url):
	urls_to_explore = parse_base_urls(url)
	corpus_of_captions = []
	for new_url in urls_to_explore:
		new_caption = return_caption(new_url)
		corpus_of_captions.append(new_caption)
	print(corpus_of_captions)
	return corpus_of_captions

if __name__ == '__main__':
	scrape_songofstyle(sys.argv[1])





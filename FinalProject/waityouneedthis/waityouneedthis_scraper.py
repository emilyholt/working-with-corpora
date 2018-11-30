from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import sys

def get_content(url):
	data = requests.get(url)
	content = data.text
	print(content)

def get_waityouneedthis_links(url):
	data = requests.get(url)
	content = data.text

	soup = BeautifulSoup(content, 'html.parser')
	links_of_interest = set()
	for link in soup.find_all('a'):		
		new_link = str(link.get('href'))
		if (new_link.startswith("http://waityouneedthis.com")):
			if (not new_link.startswith("http://waityouneedthis.com/category")) \
			and (not new_link.startswith("http://waityouneedthis.com/about")) \
			and (not new_link.startswith("http://waityouneedthis.com/page")) \
			and (not new_link.startswith("http://waityouneedthis.com/press")) \
			and (not new_link.startswith("http://waityouneedthis.com/contact")) \
			and (not new_link.endswith(".jpg")) \
			and (not new_link.endswith("#respond")) \
			and (new_link != 'http://waityouneedthis.com/') \
			and (new_link != 'http://waityouneedthis.com') \
			and (new_link != 'http://waityouneedthis.com/under-200/') \
			and (new_link != 'http://waityouneedthis.com/home-decor/') \
			and (new_link != 'http://waityouneedthis.com/splurge-worthy/'):
				links_of_interest.add(new_link)
	return links_of_interest

def get_waityouneedthis_paragraphs(url):
	'''
	Returns available urls for visible pictures
	'''

	data = requests.get(url)
	content = data.text
	soup = BeautifulSoup(content, 'html.parser')
	blog_paragraphs = []
	for paragraph in soup.find_all('p'):		
		text = str(paragraph.text)
		if not text.startswith(" Notify me") and not text.startswith("© Copyright") and not text.endswith("Turn on your JavaScript to view content\n\n"):
			if text.endswith("Comments") or text.endswith("Comment"):
				break
			if text.startswith("Leave a Comment"):
				break
			else:
				print(text)
				blog_paragraphs.append(text)
				# print("\n#########################################################\n")
	# print("\n#########################################################\n")
	return blog_paragraphs

def scrape_waityouneedthis(url):
	f = open("waityouneedthis_content.txt", 'a')
	new_links = get_waityouneedthis_links(url)
	for link in new_links:
		# print(links)
		# if len(link) >= 1:
			content = get_waityouneedthis_paragraphs(link)
			if len(content) >= 1:
				f.write(content[0])
				f.write("\n\n")
	f.close()
	print("Complete!")



if __name__ == '__main__':
	for i in range(1, 21):
		print("Processing Page # %d" % i)
		url = str(sys.argv[1]) + "/page/" + str(i)
		scrape_waityouneedthis(url)
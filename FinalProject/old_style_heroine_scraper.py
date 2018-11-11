from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import sys

def get_content(url):
	data = requests.get(url)
	content = data.text
	print(content)

def get_styleheroine_paragraphs(url):
	data = requests.get(url)
	content = data.text

	soup = BeautifulSoup(content, 'html.parser')
	# print(content)
	paragraphs_per_page = []
	for paragraph in soup.find_all('p'):		
		content = paragraph.text
		if (content != "Our weekly newsletter is full of interesting posts and fashion reports from all over the world.") and (content != "View the editorial"):
			paragraphs_per_page.append(content)
			print("Paragraph: ")
			print(content)
	return paragraphs_per_page

# def get_styleheroine_paragraphs(url):
# 	'''
# 	Returns available urls for visible pictures
# 	'''
# 	blog_content = []
# 	data = requests.get(url)
# 	content = data.text
# 	article_body_pattern = re.compile("\"articleBody\": \"(.*?)\"")
# 	blog_paragraphs = article_body_pattern.findall(content)
# 	# print(blog_paragraphs)
# 	return blog_paragraphs

def scrape_styleheroine(url):
	f = open("styleheroine_content.txt", 'a')
	new_paragraphs = get_styleheroine_paragraphs(url)
	for paragraph in new_paragraphs:
		f.write(paragraph)
		f.write("\n\n")
	f.close()
	print("Complete!")



if __name__ == '__main__':
	for i in range(1, 2):
		print("Processing Page # %d" % i)
		url = str(sys.argv[1]) + "/page/" + str(i)
		scrape_styleheroine(url)
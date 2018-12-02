import sys
import numpy as np
import matplotlib.pyplot as plt

def product_frequency_graph():
	products = ["jeans", "denim", "pants", "dress", "skirt", "shirt", "top", "bottoms", "bag", "scarf", "sunglasses", "shoes", "sneakers", "flats", "heels", "boots", "coat", "jacket", "sweater", "accessories"]
	N = (len(products))

	sos_mentions =  [58, 57, 24, 167, 43, 26, 101, 0, 98, 0, 22, 24, 12, 10, 18, 44, 26, 15, 36, 7]
	wynt_mentions = [39, 79, 23, 233, 47, 26, 162, 0, 118, 12, 46, 14, 14, 3, 29, 61, 45, 49, 79, 12]
	sh_mentions =   [8, 14, 23, 71, 8, 14, 27, 0, 42, 0, 7, 18, 4, 3, 1, 27, 10, 16, 4, 2]

	sos_averages =  [mention / sum(sos_mentions) for mention in sos_mentions]
	wynt_averages = [mention / sum(wynt_mentions) for mention in wynt_mentions]
	sh_averages =   [mention / sum(sh_mentions) for mention in sh_mentions]
	
	index = np.arange(N)    # the x locations for the groups
	width = 0.35       		# the width of the bars: can also be len(x) sequence

	fig, ax = plt.subplots()

	rects1 = plt.bar(index, sos_averages, width,
	                 color='b',
	                 label='Song of Style')

	rects2 = plt.bar(index + width, wynt_averages, width,
	                 color='r',
	                 label='Wait, You Need This')

	rects3 = plt.bar(index + width*2, sh_averages, width,
	                 color='g',
	                 label='Style Heroine')

	plt.xlabel('Product')
	plt.ylabel('Average number of Mentions of Product')
	plt.title('Average number of Mentions of Product per Blog')
	plt.xticks(range(len(products)), products, rotation=45)
	plt.legend()

	plt.tight_layout()
	plt.show()

if __name__ == '__main__':
	product_frequency_graph()
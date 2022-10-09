"""
File: web_crawler_avg.py
Name: Shane Liu
-------------------------
This file demonstrates how to get averages on www.imdb.com/chart/top.
Do you know the average score of 250 movies?
Let's use Python code to find out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html, features='html.parser')

	items = soup.find_all('td', {'class': 'ratingColumn imdbRating'})
	total = 0
	for item in items:
		target = item.strong.text  # item.text: 唯一文字資訊，不需額外指定至strong
		total += float(target)
	print('Avg (250 top movies): ', total/250)


if __name__ == '__main__':
	main()

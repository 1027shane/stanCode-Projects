"""
File: web_crawler_avg.py
Name: Shane Liu
-------------------------
This file demonstrates how to get the years who appear on www.imdb.com/chart/top most frequently!
Do you know who is the top one?
Let's use Python code to dig out the answer.
"""

import requests
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top/'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html, features='html.parser')

	items = soup.find_all('td', {'class': 'titleColumn'})
	d = {}
	for item in items:
		target = item.span.text  # <span>欄位, 取其text內容
		if target in d:
			d[target] += 1
		else:
			d[target] = 1

	for key, value in sorted(d.items(), key=lambda ele: ele[1]):
		print(key, '--->', value)


if __name__ == '__main__':
	main()

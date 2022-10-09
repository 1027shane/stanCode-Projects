"""
File: rotten_tomato.py
Name: Shane Liu
-------------------------
This file shows basic AI in classification task: movie review classification.
(1)tokenize the review, (2)count each token and give them corresponding scores
Finally, (3)calculate the score for each word,
such that we can predict a movie review by summing over the scores.
"""

# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	word_d = {}
	all_d = {
		'positive': [],
		'neutral': [],
		'negative': []
	}
	with open(FILENAME, 'r') as f:
		for line in f:
			lst = line.split(':')
			score = int(lst[0][1:3])
			review = lst[1]
			tokens = review.split()
			for token in tokens:
				token = token.lower()
				new_token = ''
				for ch in token:
					if ch.isalpha():
						new_token += ch
				if new_token not in word_d:
					word_d[new_token] = score
				else:
					word_d[new_token] += score

	for word, score in word_d.items():
		if score > 0:
			all_d['positive'].append(word)
		elif score == 0:
			all_d['neutral'].append(word)
		else:
			all_d['negative'].append(word)

	for key, value in all_d.items():
		print(key)
		print(value)
		print('-------------------')


if __name__ == '__main__':
	main()

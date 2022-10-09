"""
File: average_grades.py
Name: Shane Liu
-------------------------
This file stores all the scores in a python list
and calculates the average of all elements in it.
"""

# Constant
EXIT = -1  # Controls when to break the loop of score input


def main():
	print(f"This program averages the input(s), or {EXIT} to exit")
	lst = []
	while True:
		score = int(input('score: '))
		if score == EXIT:
			break
		lst.append(score)
	print('The average:', average_by_index(lst))
	print('The average:', average_by_for_each(lst))


def average_by_index(scores):
	"""
	:param scores: list, containing all the scores input by user
	:return : float, the average of the elements in scores
	"""
	total = 0
	for i in range(len(scores)):
		total += scores[i]
	return total/len(scores)


def average_by_for_each(scores):
	"""
	:param scores: list, containing all the scores input by user
	:return : float, the average of the elements in scores
	"""
	total = 0
	for score in scores:
		total += score
	return total/len(scores)


if __name__ == '__main__':
	main()

"""
File: word_occurrence.py
Name: Shane Liu
-------------------------
This program puts data in a text file into a nested data structure,
where key is the name of each word in romeojuliet.txt,
and the value is the dict that stores occurrence in words.
"""

# The file name of our target text file
FILE = 'romeojuliet.txt'
# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	word_count = {}
	with open(FILE, 'r') as f:
		for line in f:
			tokens = line.split()
			for token in tokens:
				# remove punctuation
				token = string_manipulation(token)
				if token not in word_count:
					word_count[token] = 1
				else:
					word_count[token] += 1
		print_out_d(word_count)


def string_manipulation(s):
	# case-insensitive
	s = s.lower()
	ans = ''
	for ch in s:
		if ch.isalpha() or ch.isdigit():
			ans += ch
	return ans


def print_out_d(d):
	"""
	: param d: dict, key of type str is a word, value of type int is the word occurrence
	"""
	# ele = ['A'=3, 'B'=4....]
	# Method 1: function
	for key, value in sorted(d.items(), key=get_index_1):
		print(key, '-->', value)
	# Method 2: lambda
	for key, value in sorted(d.items(), key=lambda ele: ele[1]):
		print(key, '-->', value)


def get_index_1(ele):
	return ele[1]


if __name__ == '__main__':
	main()

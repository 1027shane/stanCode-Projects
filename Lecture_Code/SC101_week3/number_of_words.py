"""
File: number_of_words.py
Name: Shane Liu
-------------------------
This file calculates the number of words in romeojuliet.txt by using word.split()
and basic Python list operations.
"""

FILE = 'romeojuliet.txt'


def main():
    total = 0
    with open(FILE, 'r') as f:
        for line in f:
            tokens_list = line.split()
            total += len(tokens_list)
        print('Total: ', total)


if __name__ == '__main__':
    main()

"""
File: adv_permutation.py
Name: Shane Liu
-------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking through 
(1)choose, (2)explore, and (3)un-choose.
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	permutation_helper(lst, [], len(lst))


def permutation_helper(lst, current_lst, ans_len):
	if len(current_lst) == ans_len:
		print(current_lst)
	else:
		for num in lst:
			if num in current_lst:
				pass
			else:
				# Step1: choose
				current_lst.append(num)
				# Step2: explore
				permutation_helper(lst, current_lst, ans_len)
				# Step3: un-choose
				current_lst.pop()


if __name__ == '__main__':
	main()

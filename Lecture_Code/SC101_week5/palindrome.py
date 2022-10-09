"""
File: palindrome.py
Name: Shane Liu
-------------------------
This program prints the answers of whether the strings are palindrome,
using a recursive function called is_palindrome(s).

Note: What is the self-similarity in this problem?
"""


def main():
	print(is_palindrome('madam'))             # True
	print(is_palindrome('step on no pets'))   # True
	print(is_palindrome('QQ'))                # True
	print(is_palindrome('pythonpy'))          # False
	print(is_palindrome('notion'))            # False


def is_palindrome(s):
	# self-similarity
	if len(s) == 0:
		return True
	elif len(s) == 1:
		return True
	else:
		if s[0] != s[len(s)-1]:
			return False
		return is_palindrome(s[1:len(s)-1])  # 若無return則無法逐層回傳布林值


if __name__ == '__main__':
	main()

"""
File: student_info_dict.py
Name: Shane Liu
-------------------------
This program puts data in a text file into a nested data structure,
where key is the name of each student,
and the value is the dict that stores the student info.
"""

# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}
	with open(FILE, 'r') as f:
		for line in f:
			info_lst = line.split()

			# Method 1:
			name = info_lst[0]
			age = info_lst[1]
			email = info_lst[2]
			food = info_lst[3:]
			d_name = {}
			print(hex(id(d_name)))  # id()預設為10進位
			d_name['AGE'] = age
			d_name['EMAIL'] = email
			d_name['FOOD'] = food
			all_d[name] = d_name

			# Method 2:
			all_d[info_lst[0]] = {
				'AGE': info_lst[1],
				'EMAIL': info_lst[2],
				'FOOD': info_lst[3:]
			}
	print_out_d(all_d)


def print_out_d(d):
	"""
	: param d: dict, key: str, the name of student, value: dict, the info of the student
	"""
	for name, d_name in d.items():
		print(name)
		print(d_name)
		print('--------------------------------')


if __name__ == '__main__':
	main()

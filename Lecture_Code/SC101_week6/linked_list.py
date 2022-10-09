"""
File: linked_list.py
Name: Shane Liu
-------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	# Method 1:
	node1 = ListNode(('A', 3), None)
	node2 = ListNode(('B', 5), None)
	node3 = ListNode(('C', 7), None)
	node1.next = node2
	node2.next = node3
	linked_list = node1
	traversal(linked_list)

	# Method 2:
	node3 = ListNode(('C', 7), None)
	node2 = ListNode(('B', 5), node3)
	node1 = ListNode(('A', 3), node2)
	linked_list = node1
	traversal(linked_list)

	# Method 3:
	linked_list = None
	linked_list = ListNode(('A', 3), None)
	linked_list.next = ListNode(('B', 5), None)
	linked_list.next.next = ListNode(('C', 7), None)
	traversal(linked_list)


def traversal(linked_list):
	cur = linked_list  # avoid memory leak
	# Method 1:
	# while cur.next is not None:
	# 	print(cur.val)
	# 	cur = cur.next
	# print(cur.val)
	
	# Method 2:
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()

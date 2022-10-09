"""
File: tree.py
Name: Shane Liu
-------------------------
This file shows the basic concepts for binary trees.
After constructing a tree, we will do 4 traversal examples:
(1)Pre-order
(2)In-order: Sorted 
(3)Post-order
(4)BFS
"""


class TreeNode:
	def __init__(self, left, value, right):
		self.val = value
		self.right = right
		self.left = left


def main():
	# Milestone 1: Construct a tree
	root = None
	leaf1 = TreeNode(None, 2, None)
	leaf2 = TreeNode(None, 6, None)
	leaf3 = TreeNode(None, 18, None)
	leaf4 = TreeNode(None, 40, None)

	node1 = TreeNode(leaf1, 4, leaf2)
	node2 = TreeNode(leaf3, 19, leaf4)

	root = TreeNode(node1, 17, node2)
	# Milestone 2: 3 ways to traverse a tree
	print('\n--------(1)Pre-order--------')
	pre_order(root)
	print('\n--------(2)In-order---------')
	in_order(root)
	print('\n--------(3)Post-order-------')
	post_order(root)

	# Milestone 3: Breadth First Search
	print('\n--------(4)BFS--------------')
	bfs(root)


def pre_order(root):
	if root is None:
		pass
	else:
		print(root.val, end=',')
		pre_order(root.left)
		pre_order(root.right)


def in_order(root):
	if root is None:
		pass
	else:
		in_order(root.left)
		print(root.val, end=',')
		in_order(root.right)


def post_order(root):
	if root is None:
		pass
	else:
		post_order(root.left)
		post_order(root.right)
		print(root.val, end=',')


def bfs(root):
	queue = [root]
	while len(queue) != 0:
		# dequeue(GET)
		ele = queue.pop(0)
		print(ele.val, end=',')
		# enqueue left(ADD in-order)
		if ele.left is not None:
			queue.append(ele.left)
		# enqueue right(ADD in-order)
		if ele.right is not None:
			queue.append(ele.right)


if __name__ == '__main__':
	main()

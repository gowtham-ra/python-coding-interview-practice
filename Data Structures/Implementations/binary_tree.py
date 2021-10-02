from queue import Queue
from stack import Stack

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:
	def __init__(self, data):
		self.root = Node(data)


	def pre_order_print(self, node, traversal):
		"""ROOT-->LEFT-->RIGHT
		"""
		if node:
			traversal += (str(node.data) + '-')
			traversal = self.pre_order_print(node.left, traversal)
			traversal = self.pre_order_print(node.right, traversal)
		
		return traversal

	def in_order_print(self, node, traversal):
		"""LEFT-->ROOT-->RIGHT
		"""
		if node:
			traversal = self.in_order_print(node.left, traversal)
			traversal += (str(node.data) + '-')
			traversal = self.in_order_print(node.right, traversal)

		return traversal

	def post_order_print(self, node, traversal):
		"""LEFT-->RIGHT-->ROOT
		"""
		if node:
			traversal = self.post_order_print(node.left, traversal)
			traversal = self.post_order_print(node.right, traversal)
			traversal += (str(node.data) + '-')

		return traversal


	def level_order_traversal(self, node):
		if not node:
			return

		que = Queue()
		que.enqueue(node)
		traversal = ''

		while not que.is_empty():
			node = que.dequeue()
			traversal += (str(node.data) + '-')

			if node.left:
				que.enqueue(node.left)
			if node.right:
				que.enqueue(node.right)

		return traversal

	def reverse_level_order_traversal(self, node):
		if not node:
			return

		queue = Queue()
		queue.enqueue(node)

		stack = Stack()
		traversal = ""

		while not queue.is_empty():
			traverse_node = queue.dequeue()

			stack.push(traverse_node)

			if traverse_node.right:
				queue.enqueue(traverse_node.right)
			if traverse_node.left:
				queue.enqueue(traverse_node.left)

		while not stack.is_empty():
			cur_node = stack.pop()

			traversal += (str(cur_node.data) + '-')
		
		return traversal


	def height(self, node):
		if not node:
			return -1

		return 1 + max(self.height(node.left), self.height(node.right))

	def size_rec(self, node):
		if not node:
			return 0

		return 1 + self.size_rec(node.left) + self.size_rec(node.right)

	def size_itr(self, node):
		stack = Stack()
		stack.push(node)
		size = 0

		while not stack.is_empty():
			node = stack.pop()
			size += 1

			if node.left:
				stack.push(node.left)
			if node.right:
				stack.push(node.right)

		return size


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.pre_order_print(tree.root, ''))
print(tree.in_order_print(tree.root, ''))
print(tree.post_order_print(tree.root, ''))
print(tree.level_order_traversal(tree.root))
print(tree.reverse_level_order_traversal(tree.root))
print(tree.height(tree.root))
print(tree.size_rec(tree.root))
print(tree.size_itr(tree.root))

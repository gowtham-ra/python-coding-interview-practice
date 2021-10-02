class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self, data):
		self.root = Node(data)


	def insert(self, node, value):
		if value <= node.data:
			if node.left:
				self.insert(node.left, value)
			else:
				node.left = Node(value)
		else:
			if node.right:
				self.insert(node.right, value)
			else:
				node.right = Node(value)
				

	def search(self, node, value):
		if node:
			if node.data == value:
				return True
			elif node.data < value:
				return self.search(node.right, value)
			else:
				return self.search(node.left, value)
		else:
			return False


	def in_order_print(self, node):
		if node:
			self.in_order_print(node.left)
			print(node.data)
			self.in_order_print(node.right)


	def is_bst(self):
		def is_bst_(node):
			if node:
				if node.left:
					if node.left.data < node.data:
						return is_bst_(node.left)
					else:
						return False
				if node.right:
					if node.right.data > node.data:
						return is_bst_(node.right)
					else:
						return False
			
			return True

		return is_bst_(self.root)


bst = BST(10)
bst.insert(bst.root, 5)
bst.insert(bst.root, 15)
bst.in_order_print(bst.root)
print(bst.search(bst.root, 20))
print(bst.is_bst())



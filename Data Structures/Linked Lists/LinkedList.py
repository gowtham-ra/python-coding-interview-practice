from Node import Node

class LinkedList:
	def __init__(self):
		self.head = None

	# Getter for head
	def get_head(self):
		return self.head

	# Check if the list is empty
	def is_empty(self):
		return self.head is None

	# Print all the elements data from the list
	def print_list(self):
		if self.is_empty():
			print("The list is empty!")
			return
	
		cur = self.get_head()
		while cur:
			print(cur.data, end=" -> ")
			cur = cur.next
		print("None")

	def insert_at_head(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node








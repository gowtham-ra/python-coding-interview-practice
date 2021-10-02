"""
QUEUE DATA STRUCTURE IMPLEMENTATON
"""

class Queue(object):
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		return self.items.append(item)

	def dequeue(self):
		if self.is_empty():
			print('The queue is empty')
			return
		else:
			return self.items.pop(0)

	def peek(self):
		if self.is_empty():
			print('The queue is empty')
			return
		else:
			return self.items[0].data # .data only for the sake of usage in BT

	def is_empty(self):
		return not self.items

	def size(self):
		return len(self.items)

	def __len__(self):
		return self.size()


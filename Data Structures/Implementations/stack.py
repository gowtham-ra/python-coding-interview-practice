"""
Stack Data Structure
"""

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return not self.items

	def push(self, item):
		self.items.append(item)

	def peek(self):
		if self.is_empty():
			return "The stack is empty!"
		else:
			return self.items[-1]

	def pop(self):
		if self.is_empty():
			return "The stack is empty!"
		else:
			return self.items.pop()	

	#Test Function
	def get_stack(self):
		return self.items 	

if __name__ == '__main__':
	my_stack = Stack()
	my_stack.push('A')
	my_stack.push('B')
	my_stack.push('C')
	my_stack.push('D')
	print(my_stack.get_stack())
	print(my_stack.peek())
	print(my_stack.pop())
	print(my_stack.peek())
	print(my_stack.get_stack())


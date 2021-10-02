class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None


	def append(self, data):
		node = Node(data)

		if not self.head:
			self.head = node
			return

		last = self.head

		while last.next:
			last = last.next

		last.next = node
		node.prev = last


	def prepend(self, data):
		node = Node(data)

		if not self.head:
			self.head = node
		else:
			self.head.prev = node
			node.next = self.head
			self.head = node


	def print_list(self):
		cur = self.head

		while cur:
			print(cur.data)
			cur = cur.next


	def add_after_node(self, key, data):
		cur = self.head

		while cur and cur.data != key:
			cur = cur.next

		if not cur:
			print('The given key is not in the list')
			return

		if not cur.next:
			self.append(data)
			return

		node = Node(data)
		nxt = cur.next
		
		node.next = nxt
		node.prev = cur
		cur.next = node
		nxt.prev = node

	def add_before_node(self, key, data):
		cur = self.head

		while cur and cur.data != key:
			cur = cur.next

		if not cur:
			print('The given key is not in the list')
			return

		if not cur.prev:
			self.prepend(data)
			return

		node = Node(data)
		prev = cur.prev

		node.next = cur
		node.prev = prev
		prev.next = node
		cur.prev = node

	def delete(self, key):
		cur = self.head

		# Case 1: list has no items
		if not cur:
			print("The list is empty")
			return

		# Case 2: list has only 1 item and remove that
		if (not cur.next) and (cur.data == key):
			del cur
			self.head = None
			return

		# Case 3: list has many items and remove head
		if (cur.next) and (cur.data == key):
			self.head = cur.next
			self.head.prev = None
			del cur  #or should I use cur = None?
			return

		while cur and cur.data != key:
			cur = cur.next

		# Case 4: list has many items and remove last node
		if not cur.next:
			prev = cur.prev
			del cur
			prev.next = None
			return

		# Case 5: list has many items and remove node except head or last
		prev = cur.prev
		nxt = cur.next
		
		del cur

		prev.next = nxt
		nxt.prev = prev


	def reverse(self):
		cur = self.head
		
		if not cur:
			return
		if not cur.next:
			return

		prev = None
		nxt = cur.next

		while nxt:
			cur.next = prev
			cur.prev = nxt
			
			prev = cur
			cur = nxt
			nxt = cur.next

		cur.next = prev
		cur.prev = nxt
		self.head = cur



dblist = DoublyLinkedList()
dblist.append(1)
dblist.append(2)
dblist.append(3)
dblist.append(4)
dblist.prepend(0)
dblist.print_list()

print()
dblist.reverse()
dblist.reverse()
dblist.add_after_node(2, 2.5)
dblist.add_before_node(2,1.5)
dblist.delete(1.5)
dblist.delete(2.5)
dblist.print_list()




























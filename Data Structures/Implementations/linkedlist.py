class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None


	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			last_node = self.head

			while last_node.next:
				last_node = last_node.next

			last_node.next = new_node


	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node


	def insert_after_node(self, prev_node, data):
		if not prev_node:
			print("Previous node does not exist")
			return

		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node


	def delete_node(self, key):
		cur_node = self.head

		if (cur_node) and (cur_node.data == key):
			self.head = self.head.next
			del cur_node
			return

		prev_node = None
		while cur_node and cur_node.data != key:
			prev_node = cur_node
			cur_node = cur_node.next

		if not cur_node:
			print("Value not present in the list")
			return

		prev_node.next = cur_node.next
		del cur_node


	def delete_node_at_idx(self, idx):
		cur_node = self.head
		
		if (cur_node) and (idx==0):
			self.head = self.head.next
			del cur_node
			return

		cur_idx = 0
		prev_node = None

		while (cur_node) and (cur_idx!=idx):
			prev_node = cur_node
			cur_node = cur_node.next
			cur_idx += 1

		if not cur_node:
			print("Index out of range")
			return

		prev_node.next = cur_node.next
		del cur_node


	def print_list(self):
		if not self.head:
			print("The list is empty")
		else:
			traverse = self.head

			while traverse:
				print(traverse.data)
				traverse = traverse.next


	def len_itr(self):
		cur_node = self.head
		length = 0

		while cur_node:
			length += 1
			cur_node = cur_node.next

		return length


	def len_rec(self, node):
		if not node:
			return 0

		return self.len_rec(node.next) + 1


	#Do it again and again until it becomes 2nd nature
	def swap_nodes(self, value1, value2):
		if value1 == value2:
			return

		prev_1 = None
		cur_1 = self.head

		while cur_1 and cur_1.data != value1:
			prev_1 = cur_1
			cur_1 = cur_1.next

		prev_2 = None
		cur_2 = self.head

		while cur_2 and cur_2.data != value2:
			prev_2 = cur_2
			cur_2 = cur_2.next

		if (not cur_1) or (not cur_2):
			print('One of the values does not exist in the list')
			return

		if prev_1:			
			prev_1.next = cur_2
		else:
			self.head = cur_2

		if prev_2:
			prev_2.next = cur_1
		else:
			self.head = cur_1

		cur_1.next, cur_2.next = cur_2.next, cur_1.next


	def reverse_itr(self):
		prev = None
		cur = self.head

		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt

		self.head = prev


	def reverse_rec(self):
		prev = None
		cur = self.head

		def _reverse_rec(prev, cur):
			if not cur:
				return prev

			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			return _reverse_rec(prev, cur)

		self.head = _reverse_rec(prev, cur)

	#creates a new list
	# def merge_sorted(self, other):
	# 	P = self.head
	# 	Q = other.head
	# 	new_list = LinkedList()
	# 	new_list.head = None

	# 	if not P:
	# 		return self
	# 	elif not Q:
	# 		return other

	# 	if P.data < Q.data:
	# 		new_list.head = P
	# 		P = P.next
	# 	else:
	# 		new_list.head = Q
	# 		Q = Q.next

	# 	S = new_list.head

	# 	while P and Q:
	# 		if P.data < Q.data:
	# 			S.next = P
	# 			S = P
	# 			P = P.next
	# 		else:
	# 			S.next = Q
	# 			S = Q
	# 			Q = Q.next

	# 	if not P:
	# 		S.next = P
	# 	elif not Q:
	# 		S.next = Q

	# 	return new_list

	def merge_sorted(self, other):
		P = self.head
		Q = other.head
		S = None

		if not P:
			return Q
		elif not Q:
			return P

		if P.data < Q.data:
			S = P
			P = P.next
		else:
			S = Q
			Q = Q.next

		new_head = S

		while P and Q:
			if P.data < Q.data:
				S.next = P
				S = P
				P = P.next
			else:
				S.next = Q
				S = Q
				Q = Q.next

		if not P:
			S.next = Q
		elif not Q:
			S.next = P

		self.head = new_head
		return self.head

	def remove_duplicates(self):
		elements = set()
		cur_node = self.head
		prev_node = None

		while cur_node:
			data = cur_node.data
			
			if data not in elements:
				elements.add(data)			
				prev_node = cur_node
			else:
				prev_node.next = cur_node.next
				cur_node = None
							
			cur_node = prev_node.next

	def nth_to_last_1(self, n):
		length = self.len_itr()
		cur_node = self.head

		while (cur_node) and (length!=n):
			cur_node = cur_node.next
			length -= 1

		if not cur_node:
			print('Wrong index given')
			return
		else:
			return cur_node.data

	def nth_to_last_2(self, n):
		l = self.head
		r = self.head
		count = 0

		while r and count != n:
			r = r.next
			count += 1

		if not r or not count:
			print("Wrong index given")
			return

		while r:
			r = r.next
			l = l.next

		return l.data

	def count_occurrences(self, node, data):
		if not node:
			return 0

		if node.data == data:
			return 1 + self.count_occurrences(node.next, data)
		else:
			return self.count_occurrences(node.next, data)

	def rotate(self, k):
		pivot = self.head
		count = 0

		while pivot and count < k:
			pivot = pivot.next
			count += 1

		last = pivot

		while last.next:
			last = last.next

		last.next = self.head
		self.head = pivot.next
		pivot.next = None


llist = LinkedList()
llist.append(1)
llist.append(3)
llist.append(1)
llist.append(2)
llist.append(7)
llist.append(9)
llist.append(1)
llist.append(3)
llist.remove_duplicates()
llist.print_list()
print()
print('lenghth:', llist.len_itr())
print()

N = 2
print(f'{N} to Last Idx Value = {llist.nth_to_last_1(N)}')
print(f'{N} to Last Idx Value = {llist.nth_to_last_2(N)}') 

print()
llist.rotate(1)
llist.print_list()


# print(llist.count_occurrences(llist.head, 1))
# llist.remove_duplicates()
# llist.print_list()
# llist.delete_node('A')
# llist.delete_node('A')
# llist.print_list()
# print()
# llist.delete_node_at_idx(1)
# llist.print_list()
# print('length_itr:', llist.len_itr())
# print('length_rec:', llist.len_rec(llist.head))
# llist.swap_nodes(0, 4)
# llist.reverse_itr()
# llist.print_list()
# print()
# llist.reverse_rec()
# llist.print_list()
# print()

# llist2 = LinkedList()
# llist2.append(1)
# llist2.append(3)
# llist2.append(5)
# llist2.append(7)
# llist2.print_list()
# print()
# llist2.merge_sorted(llist)
# llist2.print_list()
# print()
# llist.print_list()



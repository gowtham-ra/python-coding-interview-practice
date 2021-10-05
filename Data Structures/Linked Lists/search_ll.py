"""
Function to search the linked list for the given value
Input: lst --> linked list head, target --> value to search
Return value: Found / Not Found 
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail

def search_ll_itr(lst, target):
	cur = lst.get_head()
	while cur:
		if cur.data == target:
			return "Found"
		cur = cur.next

	return "Not Found"


def search_ll_rec(node, target):
	if node is None:
		return "Not Found"

	if node.data == target:
		return "Found"
	else:
		return search_ll_rec(node.next, target)



# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	lst.insert_at_head(-1)
	lst.print_list()
	print("ITR: 1 - " + search_ll_itr(lst, 1))
	print("ITR: 10 - " + search_ll_itr(lst, 10))
	print("\nREC: 3 - " + search_ll_rec(lst.get_head(), 3))
	print("REC: 15 - " + search_ll_rec(lst.get_head(), 15))


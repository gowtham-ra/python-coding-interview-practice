"""
Function to find the length of the given linked list
Input: lst --> linked list head
Return value: length
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail

def length(lst):
	length = 0
	cur = lst.get_head()

	while cur:
		length += 1
		cur = cur.next

	return length


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	lst.insert_at_head(-1)
	lst.print_list()
	print("Length of the list is", length(lst))

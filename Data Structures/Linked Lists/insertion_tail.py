"""
Function to insert a Node at the tail of the given linked list
Input: lst --> linked list head, value --> value to insert
Return value: None
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList

def insert_at_tail(lst, value):
	new_node = Node(value)

	if lst.is_empty():
		lst.head = new_node # Be careful: don't use "head" as variable (doesn't change actual head)
		return

	cur_node = lst.get_head()
	while cur_node.next:
		cur_node = cur_node.next
	cur_node.next = new_node


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	lst.print_list()
	insert_at_tail(lst, 0)
	lst.print_list()
	insert_at_tail(lst, 1)
	lst.print_list()
	insert_at_tail(lst, 2)
	lst.print_list()
	insert_at_tail(lst, 3)
	lst.print_list()
	lst.insert_at_head(-1)
	lst.print_list()
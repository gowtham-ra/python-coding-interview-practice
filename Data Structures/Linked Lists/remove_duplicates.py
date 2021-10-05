"""
Function to remove duplicate values from the given linkedlist
Input: lst --> linked list head
Return value: None
Technique: HashMap
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail
from deletion_by_value import delete_node

def remove_duplicates(lst):
	visited = set()
	cur_node = lst.get_head()

	while cur_node:
		value = cur_node.data

		if value in visited:
			delete_node(lst, value)
		else:
			visited.add(value)

		cur_node = cur_node.next

	return


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 3)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	lst.insert_at_head(-1)
	insert_at_tail(lst, -1)
	insert_at_tail(lst, 0)
	lst.print_list()
	remove_duplicates(lst)
	lst.print_list()







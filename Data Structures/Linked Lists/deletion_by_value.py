"""
Function to search the linked list for the given value and delete it
Input: lst --> linked list head, target --> value to search and delete
Return value: None 
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail

def delete_node(lst, value):
	if lst.is_empty():
		return "List is empty"

	prev = None
	delete = lst.get_head() # Node to delete

	# Iterate till you reach the node to delete
	while delete:
		if delete.data == value:
			break
		prev = delete
		delete = delete.next

	# If the value is not in the list		
	else:
		return "Value not found"

	# If delete node is the first node
	if prev is None:
		lst.head = lst.head.next
		delete.next = None
		del delete
		return

	prev.next = delete.next
	delete.next = None
	del delete

	return


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	lst.insert_at_head(-1)
	lst.print_list()
	print("Deleting -1")
	delete_node(lst, -1)
	lst.print_list()
	print("Deleting 2")
	delete_node(lst, 2)
	lst.print_list()





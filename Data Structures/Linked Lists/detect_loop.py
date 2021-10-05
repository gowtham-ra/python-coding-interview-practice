"""
Function to detect loop in the given linked list
Input: lst --> linked list head
Return value: Found or Not Found
Technique Used: Floyd's Cycle-Finding Algorithm
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail

def detect_loop(lst):
	if lst.is_empty():
		return "The list is empty"

	fast = slow = lst.get_head()

	while fast and slow and fast.next:
	 	slow = slow.next
	 	fast = fast.next.next

	 	if slow == fast:
	 		return True

	return False


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	insert_at_tail(lst, 4)
	lst.insert_at_head(-1)
	lst.print_list()
	print(detect_loop(lst))

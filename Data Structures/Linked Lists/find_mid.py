"""
Function to find the middle value of a linkedlist
Input: lst --> linked list head
Return value: Mid value
Technique Used: Fast and Slow Pointers
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail

def find_mid(lst):
	if lst.is_empty():
		return "The list is empty"

	slow = fast = lst.get_head()

	# If one or two elements, return the first as mid
	if slow.next is None or fast.next.next is None:
		return slow.data

	# Start from slow + 2 position
	fast = fast.next.next

	# For each move of slow, jump fast to 2 steps
	while slow:
		slow = slow.next
		fast = fast.next

		if fast:
			fast = fast.next
		else:
			break

	return slow.data


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	lst.insert_at_head(-1)
	lst.print_list()
	print(find_mid(lst))

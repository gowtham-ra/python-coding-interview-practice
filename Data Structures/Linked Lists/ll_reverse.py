"""
Function to reverse the given linked list
Input: lst --> linked list head
Return value: None
TC: O(n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail

def reverse_itr(lst):
	if lst.is_empty():
		return "The list is empty"

	prev = None
	cur = lst.get_head()

	if cur.next is None:
		return

	next = cur.next
	while next:
		cur.next = prev
		prev = cur
		cur = next
		next = next.next

	cur.next = prev
	lst.head = cur
	return


def reverse_rec(head):
	if head is None or head.next is None:
		return head

	rest = reverse_rec(head.next)
	head.next.next = head
	head.next = None
	return rest


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	lst.insert_at_head(-1)
	lst.print_list()
	print("Reversing Iteratively...")
	reverse_itr(lst)
	lst.print_list()
	print("Reversing Recursively...")
	lst.head = reverse_rec(lst.get_head())
	lst.print_list()



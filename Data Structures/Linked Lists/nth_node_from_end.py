"""
Function to return the nth node from the end
Input: lst --> linkedlist, n --> distance
Return value: nth node
TC: O(l-n) l is the length of the list
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail
import find_len

def nth_from_end(lst, n):

    if lst.is_empty():
        return -1

    nth_node = lst.get_head()  # This iterator will reach the Nth node
    end_node = lst.get_head()  # This iterator will reach the end of the list

    count = 0
    while count < n:
        if end_node is None:
            return -1
        end_node = end_node.next
        count += 1

    while end_node:
        end_node = end_node.next
        nth_node = nth_node.next

    return nth_node.data


# Test code to dry run the implementations
if __name__ == '__main__':
	lst = LinkedList()
	insert_at_tail(lst, 0)
	insert_at_tail(lst, 1)
	insert_at_tail(lst, 2)
	insert_at_tail(lst, 3)
	lst.print_list()
	print(nth_from_end(lst, 1))

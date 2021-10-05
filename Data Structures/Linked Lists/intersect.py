"""
Function to find if two linkedlists intersect
Input: lst1, lst2 --> two linked lists
Return value: Point of intersection or None
TC: O(m + n)
SC: O(1) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail
from find_len import length

def intersect(lst1, lst2):
	len1 = length(lst1)
	len2 = length(lst2)
	diff = abs(len1 - len2)

	if len1 > len2:
		longest = lst1
		other = lst2
	else:
		longest = lst2
		other = lst1

	h1 = longest.get_head()
	h2 = other.get_head()

	while diff > 0:
		h1 = h1.next
		diff -= 1

	while h1 and h2:
		if h1 is h2:
			return h1

		h1 = h1.next
		h2 = h2.next

	return None




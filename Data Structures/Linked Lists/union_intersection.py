"""
Function to find the union and intersection of two linkedlists
Input: lst1, lst2 --> Two linkedlists
Return value: None
TC: O(n)
SC: O(n) """

from Node import Node
from LinkedList import LinkedList
from insertion_tail import insert_at_tail

def union_intersection(lst1, lst2):
	union = LinkedList()
	intersection = LinkedList()
	visited = {}

	cur_node = lst1.get_head()

	while cur_node:
		value = cur_node.data

		if value not in visited:
			visited[value] = 1
			union.insert_at_head(value)

		cur_node = cur_node.next

	cur_node = lst2.get_head()

	while cur_node:
		value = cur_node.data

		if value in visited and visited[value] == 1:
			intersection.insert_at_head(value)
			visited[value] += 1
		elif value not in visited:
			visited[value] = 1
			union.insert_at_head(value)

		cur_node = cur_node.next

	print("Union:", end=' ')
	union.print_list()
	print("Intersection:", end=' ')
	intersection.print_list()

	return 


if __name__ == '__main__':
	lst1 = LinkedList()
	insert_at_tail(lst1, 0)
	insert_at_tail(lst1, 1)
	insert_at_tail(lst1, 2)
	insert_at_tail(lst1, 3)
	print("List 1:", end=' ')
	lst1.print_list()

	lst2 = LinkedList()
	insert_at_tail(lst2, 2)
	insert_at_tail(lst2, 3)
	insert_at_tail(lst2, 4)
	insert_at_tail(lst2, 5)
	print("List 2:", end=' ')
	lst2.print_list()

	union_intersection(lst1, lst2)







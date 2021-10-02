# Merge two sorted lists into a sorted list
def merge_lists(lst1, lst2):
    # Write your code here
    m = len(lst1)
    n = len(lst2)
    l1_idx, l2_idx = 0, 0
    sorted_lst = []

    while (l1_idx < m) and (l2_idx < n):
        if lst1[l1_idx] < lst2[l2_idx]:
            sorted_lst.append(lst1[l1_idx])
            l1_idx += 1
        else:
            sorted_lst.append(lst2[l2_idx])
            l2_idx += 1
    
    while l1_idx < m:
        sorted_lst.append(lst1[l1_idx])
        l1_idx += 1
    
    while l2_idx < n:
        sorted_lst.append(lst2[l2_idx])
        l2_idx += 1

    return sorted_lst
# Two sum
def find_sum(lst, k):
    # Write your code here
    hashmap = {}

    for i in range(len(lst)):
        val = k - lst[i]

        if lst[i] in hashmap:
            return [hashmap[lst[i]], lst[i]]
        else:
            hashmap[val] = lst[i]
    
    return []
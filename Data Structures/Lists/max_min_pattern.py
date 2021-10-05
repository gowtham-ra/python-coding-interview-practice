"""
Sorted list - Max min patterning in-place 

Technique learnt: Keeping two values at the same indices using modulos properties.
TC: O(n) SC: O(1) --- using the mentioned technique """

def max_min(A):
    max_idx = len(A) - 1
    min_idx = 0
    max_elem = A[-1] + 1

    for i in range(len(A)):
        # Even indices for max elements
        if i%2 == 0:
            A[i] += (A[max_idx] % max_elem) * max_elem
            max_idx -= 1

        # Odd indices for min elements
        else:
            A[i] += (A[min_idx] % max_elem) * max_elem
            min_idx += 1

    for i in range(len(A)):
        A[i] //= max_elem
"""
Maximum sum sub-array
Technique: Kadane's Algorithm
TC: O(n) SC: O(1) """

def max_sum(A):
    global_max_sum = local_max_sum = A[0]

    # Kadane's Algorithm
    for i in range(1, len(A)):
        local_max_sum = max(A[i], local_max_sum + A[i])
        global_max_sum = max(local_max_sum, global_max_sum)

    return global_max_sum
# List of Products of all Elements
def find_product(lst):
    # Write your code here
    result = []
    product = 1
    zero_count = lst.count(0)

    for num in lst:
        if num:
            product *= num
    
    if zero_count == 0:
        for num in lst:
            result.append(product // num)
    elif zero_count == 1:
        for num in lst:
            if num != 0:
                result.append(0)
            else:
                result.append(product)
    else:
        result = [0] * len(lst)

    return result
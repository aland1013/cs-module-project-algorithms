'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    d = {arr[0]: 0}
    
    for num in arr[1:]:
        if d.get(num) is not None:
            d.pop(num)
        else:
            d[num] = 0
    
    return list(d.keys())[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
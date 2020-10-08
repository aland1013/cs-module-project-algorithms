'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # first pass solution with O(n) space complexity
    # new_arr = []
  
    # for num in arr:
    #     if num == 0:
    #         new_arr.append(0)
    #     else:
    #         new_arr.insert(0, num)
  
    # return new_arr
    
    # optimized solution with O(1) space complexity
    count = 0 # counts the number of non-zero elements in arr
    
    # traverse arr from left to right
    for i in range(len(arr)):
        # if the number in arr is not 0, replace the number at
        # index 'count' with the number
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    # all non-zero numbers have been moved to the front of arr
    # and 'count' is at the index where the 0s should begin
    # fill arr from index 'count' to the end with 0s
    while count < len(arr):
        arr[count] = 0
        count += 1
    
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
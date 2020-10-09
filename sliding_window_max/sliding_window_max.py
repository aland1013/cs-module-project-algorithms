'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque

def sliding_window_max(nums, k):
    # first pass solution
    # divide nums into subarrays of length k
    # push the max of each subarray into a new array
    # return the new array
    
    # return [max(nums[i:i + k]) for i in range(0, len(nums) - k + 1)]

    # optimized solution with O(n) runtime complexity
    maxes = [] # stores max of each window
    q = deque() # stores indexes of integers in nums in decr order   
    
    # process first k integers in nums
    for i in range(k):
        
        # for each integer, remove previous smaller
        # integers from q
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        
        # add new integer to end of q
        q.append(i)
    
    # process rest of integers in nums
    for i in range(k, len(nums)):
        
        # integer at front of q is max int
        # in previous in window, so add it to
        # the list holding max of each window 
        maxes.append(nums[q[0]])
        
        # remove integers not in this window
        while q and q[0] <= i - k:
            q.popleft()
        
        # remove all integers smaller than
        # the one being added
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        
        # add current integer to the end of q
        q.append(i)
    
    # add max integer in last window
    maxes.append(nums[q[0]])
    
    return maxes         

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

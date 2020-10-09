'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # first pass solution
    
    # # cookie monster can eat n cookies three ways
    #     # by starting at n - 1 cookies and eating 1
    #     # by starting at n - 2 cookies and eating 2
    #     # by starting at n - 3 cookies and eating 3
    
    # # base case: ate too many cookies
    # if n < 0:
    #     return 0
    
    # # base case: 1 way to eat 0 cookies
    # if n == 0:
    #     return 1
    
    # # combine results of eating 1, 2, or 3 cookies at a time
    # return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    
    # optimized solution that passes large input test by using dynamic programming
    
    if cache == None:
        cache = [0 for _ in range(n + 1)]
    
    cache[0], cache[1] = 1, 1
    
    if n < 0:
        return 0
    
    if n == 0:
        return 1
    
    if cache[n - 1] == 0:
        cache[n - 1] = eating_cookies(n - 1, cache)
    
    if cache[n - 2] == 0:
        cache[n - 2] = eating_cookies(n - 2, cache)
    
    if cache[n - 3] == 0:
        cache[n - 3] = eating_cookies(n - 3, cache)
    
    cache[n] = cache[n - 1] + cache[n - 2] + cache[n - 3]
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

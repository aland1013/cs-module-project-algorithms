'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # cookie monster can eat n cookies three ways
        # by starting at n - 1 cookies and eating 1
        # by starting at n - 2 cookies and eating 2
        # by starting at n - 3 cookies and eating 3
    
    # base case: invalid input
    if n < 0:
        return 0
    
    # base case: 1 way to eat 0 cookies
    if n == 0:
        return 1
    
    # combine results of eating 1, 2, or 3 cookies at a time
    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

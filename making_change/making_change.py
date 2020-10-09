#!/usr/bin/python

import sys

def making_change(amount, denominations):
    # create a list of length amount + 1
    ways = [0 for _ in range(amount + 1)]
    
    # there is 1 way to make 0 with 0 coins
    ways[0] = 1
    
    # go through all coins in denominations list
    for i in range(len(denominations)):
        
        # compare value of the coin with each index value in ways
        for j in range(len(ways)):
            
            # if the value of the coin is less than or equal to the index value,
            # update the ways array
            if denominations[i] <= j:
                ways[j] += ways[j - denominations[i]]
    
    return ways[-1]   

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
#!/usr/bin/python

import sys
from itertools import product

def rock_paper_scissors(n):
    rounds = product(['rock', 'paper', 'scissors'], repeat=n)
    
    return [list(r) for r in rounds]
       
print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
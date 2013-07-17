#!/usr/bin/python -tt
import sys
import re
import euler
import time

def main():
  n = 10**7
  F = sequence_down_from_n(n, fib)
  num = 0
  for i in xrange(n+1):
    num += zeckendorf(F, i)
  print num

def fib():
    memo = [1, 2]
    while True:
        memo.append(sum(memo))
        yield memo.pop(0)
 
def sequence_down_from_n(n, seq_generator):
    seq = []
    for s in seq_generator():
        seq.insert(0,s)
        if s >= n: break
    return seq
 
def zeckendorf(seq, n):
    if n == 0: return 0
    digits, nleft = [], n
    num = 0
    for s in seq:
        if s <= nleft:
            num += 1
            nleft -= s
    return num


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  start = time.time()
  main()
  print 'Time taken:', time.time()-start, 'seconds'



#!/usr/bin/python -tt
import sys
import re
import euler
import time
from matplotlib import pyplot as plt

def main():
  P = euler.get_primes(1000010)

  #we are only interested in primes >=5
  P = P[2:]
  ans = 0

  for i in xrange(len(P)-1):
    p1 = P[i]
    p2 = P[i+1]
    num = find_num(p1, p2)
    ans += num
  
  print ans

def find_num(p1, p2):
  p1_s = str(p1)
  l = len(p1_s)
  num = p2
  while True:
    num += p2
    if str(num)[l:] == p1_s:
      return num

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  start = time.time()
  main()
  print 'Time taken:', time.time()-start, 'seconds'



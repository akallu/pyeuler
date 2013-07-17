#!/usr/bin/python -tt
import sys
import re
import euler
import time

def main():
  P = euler.get_primes(10**8)
  #only interested in primes from 5 onwards
  P = P[2:]
  start = time.time()
  total = 0
  for p in P:
    total += ((g(p)%p) * (euler.factorialMod(p-5, p))) % p
    #print 'prime:\t', p, 'num:\t', num

  print total
  print 'Time taken:', time.time()-start, 'seconds'

def g(n):
  return n**4 + (-9*n**3) + (27*n**2) + (-30*n) + 9

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()


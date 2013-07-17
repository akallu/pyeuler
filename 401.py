#!/usr/bin/python -tt
import sys
import re
import euler
import time
from pprint import pprint

def main():
  P = euler.get_primes(10**7.5)
  M = []
  A = {'a': 1, 'b': 10}
  B = {'a': 4, 'c': 10}
  print merge(A, B)
  for i in xrange(1, 10**2):
    M.append(decompose(M, P, i))
    print i, pprint(M[-1])

def decompose(M, P, n):
  F = {}
  if n < 1: return {1: 1}
  for p in P:
    while n % p == 0:
      if n < len(M):
        return merge(M[n-1], F)
      if p in F:
        F[p] += 1
      else:
        F[p] = 1
      n /= p
      if n == 1:
        return F

def merge(A, B):
  for a in A:
    if a in B:
      B[a] += A[a]
    else:
      B[a] = A[a]
  return B
        


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  start = time.time()
  main()
  print 'Time taken:', time.time()-start, 'seconds'



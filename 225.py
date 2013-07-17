#!/usr/bin/python -tt
import sys
import re
import euler
import time

def main():
  T = trib(10**5)
  nums = []
  i = 27
  while len(nums) < 124:
    if f(T, i):
      nums.append(i)
    i += 2

  print nums[-1]
      
  
def f(T, n):
  for t in T:
    if t%n == 0:
      return False
  return True

def trib(n):
  T = [1, 1, 1]
  while len(T) < n:
    T.append(T[-1]+T[-2]+T[-3])
  return T
 
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  start = time.time()
  main()
  print 'Time taken:', time.time()-start, 'seconds'



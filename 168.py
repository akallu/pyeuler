#!/usr/bin/python -tt
import sys
import re
import euler
import time

def main():
  for i in xrange(10**7):
    first_digit = i
    count = 0
    while first_digit >= 10:
      count += 1
      first_digit /= 10
    last_digit = i%10
    if last_digit > first_digit:
      right_rotate = (10**count)*last_digit + i/10
      if right_rotate % i == 0:
        print i, right_rotate

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  start = time.time()
  main()
  print 'Time taken:', time.time()-start, 'seconds'



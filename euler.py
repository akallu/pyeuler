import numpy as np

def get_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)].tolist()

#return a list of all fibonacci's below n
def get_fibs(n):
  a, b = 0, 1
  fibs = [b]
  while b < n:
    a, b = b, a+b
    fibs.append(b)
  return fibs

def factorialMod(n, modulus):
    ans=1
    if n <= modulus//2:
        #calculate the factorial normally (right argument of range() is exclusive)
        for i in range(1,n+1):
            ans = (ans * i) % modulus   
    else:
        #Fancypants method for large n
        for i in range(1,modulus-n):
            ans = (ans * i) % modulus
        ans = modinv(ans, modulus)

        #Since m is an odd-prime, (-1)^(m-n) = -1 if n is even, +1 if n is odd
        if n % 2 == 0:
            ans = -1*ans + modulus
    return ans % modulus

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

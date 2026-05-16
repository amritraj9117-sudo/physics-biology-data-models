import math as m
import time

def power_recur(n, p):
    """Calculates n^p recursively."""
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * power_recur(n, p - 1)

def factorial(n):
    """Calculates factorial recursively."""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(a):
    """Checks if a single number is prime."""
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def print_primes(limit):
    """Returns a list of prime numbers up to the limit."""
    primes = []
    for i in range(2, limit):
        prime_flag = True
        for j in range(2, i):
            if i % j == 0:
                prime_flag = False
                break
        if prime_flag:
            primes.append(i)
    return primes

def count_ways(n, steps, memo=None):
    """Dynamic programming: count ways to climb n stairs."""
    if memo is None:
        memo = {}
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in memo:
        return memo[n]

    count = 0
    for step in steps:
        count += count_ways(n - step, steps, memo)
    
    memo[n] = count
    return count

# --- Test Code ---
if __name__ == "__main__":
    print(f"2^10 = {power_recur(2, 10)}")
    print(f"Factorial of 5 = {factorial(5)}")
    print(f"Primes up to 50: {print_primes(50)}")
    
    start = time.perf_counter()
    print(f"Ways to climb 100 stairs (1, 2): {count_ways(100, (1, 2))}")
    print(f"Time taken: {time.perf_counter() - start:.6f} seconds")
class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
        
    def plus(self, other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom).reduce()
        
    def inverse(self):
        return self.denom / self.num
        
    def __str__(self):
        if self.denom != 1:
            return f"{self.num}/{self.denom}"
        return str(self.num)
        
    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom).reduce()
        
    def reduce(self):
        def gcd(n, d):
            while d != 0:
                n, d = d, n % d
            return n
            
        if self.denom == 0:
            return None
        elif self.num == 0:
            return Fraction(0, 1)
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num / greatest_common_divisor)
            bottom = int(self.denom / greatest_common_divisor)
            return Fraction(top, bottom)
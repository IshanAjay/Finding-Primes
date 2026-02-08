# Efficiency Booster
"""
By definition, a prime number is a number that is only divisible by 1 and itself.
Factor trees look like the following:
            36
        2   *   9
            3   *   3
This proves that if the testNumber is divisible by any non-prime number, than it is ALWAYS divisble by a prime number that is smaller than it aside form itself.
Therefore, if an array containing 'testNumber % allPrimesBeforeIt' does NOT contain 0, then it is a prime number.

Since all prime numbers aside from 2 are odd, 2 can not be a factor. This means that testNumber does NOT need to be divided by ALL primes up to it.
It only needs to be tested with primes that are < 1/2 of testNumber
"""
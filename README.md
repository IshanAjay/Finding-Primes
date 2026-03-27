# Finding Prime Numbers

This repository contains scripts that allow you to find prime numbers using Python. Please note that Python is NOT fully optimized for dealing with large numbers.

A prime number is a number that is only divisible by 1 and itself. Examples include 2, 3, 5, 7, 11, 13...

My goal is to find the largest prime number. The largest known prime is a Mersenne prime. I don't have the memory resources to find the absolute largest, however I wanted to at least figure out the logic. The big focus in this experiment is efficiency.

**Testing** means to divide the testNumber by a series of numbers (i.e. 100/2, 100/3, 100/4...). If the remainder is 0, it is divisible. If divisible by any number excluding 1 and itself, it is composite. Otherwise, it is prime. Assume numbers are real and positive only.

The easiest approach is to test every number greater than 1 but less than the testNumber. Accurate but slow.

The easiest numbers to rule out are evens except 2. Start at an odd number and add 2 each time. Add 2 to primes upfront. This rules out half the numbers.

But testing every number is still slow. Use factor trees: 36 = 2 * 3 * 2 * 3. If testNumber is divisible by any composite, it is ALWAYS divisible by a smaller prime. So only test divisibility by primes up to sqrt(testNumber), not all numbers. This drastically improves efficiency.

**Files:**
- `finding_primes.py` - Main CLI app with prime finding, checking, factorization, and multiple algorithms.
- `iterate_list.py` - Demonstrates basic list iteration with while loops.
- `test_divisibility.py` - Shows nested loops to test one number against all divisors.
- `find_primes_basic.py` - Basic prime finder using modulo to test divisibility.
- `find_1000_primes.py` - Finds first 1000 primes using the algorithm.
- `efficiency_notes.py` - Documents the sqrt optimization and prime-only testing.

No external dependencies - uses only Python standard library. Compatible with Python 3.x. Run `python3 finding_primes.py --help` for usage options.
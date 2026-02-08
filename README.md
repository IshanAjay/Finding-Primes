# Finding-Primes
This repository contains scripts that allows one to find prime numbers using Python. Please note that Python is NOT fully optimized for dealing with large numbers.
--
This script finds the first 1000 prime numbers. A prime number is a number that is only divisible by 1 and itself. Examples include 1, 2, 3, 5, 7, 11, 13, ...
My goal is to find the largest prime number. Currently, the largest prime is Mersenne52. I don't have the memory resources to find the absolute largest prime number, however I wanted to at least figure out the logic. This big focus in this experiment is efficiency.

*Testing means to divide the testNumber by a series of numbers. (i.e. 100/2, 100/3, 100/4, ...)*
*If the remainder is 0, then it is divisible by that number, else it is not.*
*If the testNumber is divided by a number that excludes 1 and itself and has a remainder of 0, it is composite.*
*Else, it is prime.*

*assume numbers refers to real, positive numbers only*


The easiest way to approach this problem is to take a testNumber and divide it by all of the numbers that are greater than 1, but less than itself. This will be accurate, however, it is the slowest it could possibly be.

The easiest numbers to rule out are even numbers except for 2. So, the testNumber should start on an odd number and add 2 each time to ensure it is always odd. In this option, 2 would need to be added to the array of primes before the project begins as if the number is odd, it does not need to be tested with 2. This is more efficeint since it rules out half the numbers.

Up until now, numbers are tested with every number, prime and composite, up to it except for 1, 2, and itself. This can be fixed using some mathematical logic. Factor trees can be used to turn a composite number into a multiplication of prime numbers.
Example:
    36
2   *  18
    3   *   6
        2   *   3
Therefore, 36 = 2 * 3 * 2 * 3. This means that when testing for prime numbers, the testNumber only needs to be divided by the prime numbers up to it except for 1, 2, and possibly itself. This drastically improves efficiency.

Since 2 was ruled out, the prime number that the testNumber is divided by must be less than half of the testNumber. This works because 2 has already been ruled out, fractions can not be used, and an exception for 1 has been created since all real numbers are divisible by 1. *This has not been implemented yet, but it is on my agenda.*

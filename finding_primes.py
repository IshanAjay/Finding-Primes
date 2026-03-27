"""Prime number finding module with CLI interface."""

import sys
import argparse


def is_prime(n, primes):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n**0.5) + 1
    for p in primes:
        if p > limit:
            break
        if n % p == 0:
            return False
    return True


def find_primes_trial_division(limit):
    if limit < 2:
        return []

    primes = [2]
    candidate = 3

    while candidate <= limit:
        if is_prime(candidate, primes):
            primes.append(candidate)
        candidate += 2

    return primes


def find_primes_sieve(limit):
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]


def find_first_n_primes(n, method="trial"):
    if n < 1:
        return []

    if n == 1:
        return [2]

    if method == "sieve":
        limit = n * (n * 2)
        primes = find_primes_sieve(limit)
        return primes[:n]

    primes = [2]
    candidate = 3

    while len(primes) < n:
        if is_prime(candidate, primes):
            primes.append(candidate)
        candidate += 2

    return primes


def prime_factorization(n):
    if n < 2:
        return []

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def is_prime_check(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Find prime numbers using various methods.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --limit 100              Find all primes up to 100
  %(prog)s --first 50               Find first 50 primes
  %(prog)s --check 17               Check if 17 is prime
  %(prog)s --factor 100             Prime factorization of 100
  %(prog)s --sieve --limit 1000     Use Sieve of Eratosthenes
  %(prog)s --output primes.txt --first 100
                                Save first 100 primes to file
        """,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--limit", type=int, help="Find all primes up to LIMIT")
    group.add_argument("--first", type=int, help="Find first N primes")
    group.add_argument("--check", type=int, help="Check if NUMBER is prime")
    group.add_argument("--factor", type=int, help="Prime factorization of NUMBER")

    parser.add_argument(
        "--sieve", action="store_true", help="Use Sieve of Eratosthenes algorithm"
    )
    parser.add_argument("-o", "--output", type=str, help="Output file path")
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Suppress additional output"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Show detailed information"
    )

    args = parser.parse_args()

    result = None
    output_text = ""

    if args.check is not None:
        result = is_prime_check(args.check)
        output_text = f"{args.check} is {'prime' if result else 'not prime'}"
        if args.verbose:
            if result and args.check > 2:
                factors = prime_factorization(args.check)
                output_text += f"\nPrime factorization: {' x '.join(map(str, factors))}"

    elif args.factor is not None:
        if args.factor < 2:
            output_text = "Numbers less than 2 have no prime factorization"
        else:
            factors = prime_factorization(args.factor)
            output_text = f"{args.factor} = {' x '.join(map(str, factors))}"

    elif args.limit is not None:
        if args.limit < 2:
            result = []
        elif args.sieve:
            result = find_primes_sieve(args.limit)
        else:
            result = find_primes_trial_division(args.limit)

        output_text = str(result)
        if not args.quiet:
            output_text += f"\nPrimes found: {len(result)}"

    elif args.first is not None:
        method = "sieve" if args.sieve else "trial"
        result = find_first_n_primes(args.first, method)

        output_text = str(result)
        if not args.quiet:
            output_text += f"\nPrimes found: {len(result)}"
            if args.verbose:
                output_text += f"\nLargest: {result[-1] if result else 'N/A'}"

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_text)
        if not args.quiet:
            print(f"Output written to {args.output}")

    print(output_text)


if __name__ == "__main__":
    main()

# Finds the first 1000 prime numbers
PRIMES = [1]
PARENT_LIST = [3, 5]
testnumber = 7


i = 0
while len(PARENT_LIST) < 999:
    TEST_LIST = []
    n = 0
    while n < len(PARENT_LIST):
        TEST_LIST.append (testnumber % PARENT_LIST[n])
        n += 1

    if 0 in TEST_LIST:
        testnumber += 2
    else:
        PARENT_LIST.append (testnumber)
        testnumber += 2

PRIMES += PARENT_LIST
print(PRIMES)
print("Primes found:", len(PRIMES))
# Dividing a number by all values in a list before moving on to another number unless
# that number has a non-zero remainder when divided by all numbers in that list.
# If so, it should be added to the parent list and the parent list should be printed.

PARENT_LIST = [3, 5]
testnumber = 7


i = 0
for i in range(10):
    # Test 
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

print(PARENT_LIST)
print("Primes found:", len(PARENT_LIST))
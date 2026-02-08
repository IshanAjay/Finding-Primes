# How to test all items in list on one number before moving to the next

list = [1, 2, 3, 5]
lenList = len(list)
n = 0

testSubject = 6

while lenList < 5:
    while n < lenList:
        print(testSubject / list[n])
        n += 1

    n = 0
    testSubject += 1
# Euler 4

import math


def ispalindrome(num):
    stringnum = str(num)
    for i in range(math.floor(stringnum.__len__() / 2)):
        if not stringnum[i] == stringnum[(-1 * i - 1)]:
            return False
    return True


print(ispalindrome(758857))
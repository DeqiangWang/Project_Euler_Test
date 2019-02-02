# Euler 4

import math
import time


def ispalindrome(num):
    stringnum = str(num)
    for i in range(math.floor(stringnum.__len__() / 2)):
        if not stringnum[i] == stringnum[(-1 * i - 1)]:
            return False
    return True


def digit_count(num):
    return int(len(str(num)))


# main
def main():
    for max_pal_candidate in range(999 * 999, 100 * 100, -1):
        if ispalindrome(max_pal_candidate):
            # the fact that palindrome of 6 digits/5 digits are divisible by 11
            for divisor in range(110, 990, 11):
                if (max_pal_candidate % divisor) == 0:
                    if digit_count(int(max_pal_candidate / divisor)) == 3:
                        print(max_pal_candidate)
                        return


start_time = time.time()
main()
print("Time elapsed:" + str(time.time() - start_time))
eul4 = "YnkgV2lkeWEgQWdlbmcgU2V0eWEgVHV0dWtv"

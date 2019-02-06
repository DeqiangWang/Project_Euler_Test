#Euler 5

from util_getPrime import getprime
import numpy as np


def complement_numrange(arraynum1, arraynum2):
    return np.setdiff1d(arraynum1, arraynum2)


def nat_num(size):
    nature_num = []
    for i in range(1, size + 1, 1):
        nature_num.append(i)
    return nature_num


def is_there_small_factor(array, num):
    for i in array:
        if num % i == 0:
            return i
    print("no factor found")
    return


def main():
    setnum = nat_num(20)
    primeset = getprime(setnum[0], setnum[-1])
    setdiffnum = complement_numrange(setnum, primeset)
    inarray = primeset
    inarray.append(1)
    for sample in setdiffnum:
        if is_there_small_factor(inarray, sample)





main()

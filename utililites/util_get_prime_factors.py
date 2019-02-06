# Utility 2
from utililites.util_get_prime import isprime
import numpy as np


# to return original prime factors, without removing duplicates
def get_prime_factors(num):
    primefactor = []
    for index in range(2, num+1):
        if isprime(index):
            if (num % index) == 0:
                primefactor.append(index)
                num = int(num/index)
                while (num % index) == 0:
                    primefactor.append(index)
                    num = int(num/index)
                    if num == 1:
                        return primefactor
    return primefactor


# to return unique prime factors of a number
def get_prime_factors_unique(num):
    return np.unique(get_prime_factors(num))

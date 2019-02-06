# Utility 3
from utililites.util_get_prime_factors import get_prime_factors


# Getting the prime factors in intersection set, or simply a gcd call
def get_gcd(num1, num2):
    return list((get_prime_factors(num1)) or (get_prime_factors(num2)))

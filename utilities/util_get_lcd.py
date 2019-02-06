# Utility 3
from utilities.util_get_prime_factors import get_prime_factors
from utilities.util_get_diff_elements import get_comp_array
from functools import reduce


# Getting the prime factors in intersection set, or simply a gcd call
def get_lcd(num1, num2):
    value = get_comp_array(get_prime_factors(num1), get_prime_factors(num2))
    if value is None:
        return
    return int(reduce(lambda a, b: a*b, value))


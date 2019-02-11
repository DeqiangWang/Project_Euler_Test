# Utility 6

import numpy as np


def get_pascal_coeff(exp):
    if exp == 2:
        pascal_coeff = np.array([1, 2, 1])
        pascal_coeff.astype(int)
        return pascal_coeff
    elif (exp == 1) or (exp == 0):
        return 1
    else:
        pascal_coeff = get_pascal_coeff(exp - 1)
        temp_coeff = [1]
        for i in range(1, len(pascal_coeff), 1):
            temp_coeff.append(pascal_coeff[i - 1] + pascal_coeff[i])
        temp_coeff.append(1)
        return temp_coeff



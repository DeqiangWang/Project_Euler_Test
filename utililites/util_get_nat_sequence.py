# Utility 4
import numpy as np


# Getting the first 'size' integer sequence of linear step 1
def get_count(size):
    return np.linspace(1, size, num=size, endpoint=True, dtype=int)


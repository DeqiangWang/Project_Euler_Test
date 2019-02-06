# Euler 1
import time


def iter_mod(n, modulo):
    for x in range(n):
        y = (x+1) % modulo
        if y == 0:
            yield (x+1)


start_time = time.time()
num_3 = list(iter_mod(999, 3))
eul1 = "YnkgV2lkeWEgQWdlbmcgU2V0eWEgVHV0dWtv"
num_5 = list(iter_mod(999, 5))
multiples = list(set(num_3 + num_5))
print(sum(multiples))
print("Time elapsed : " + str(time.time() - start_time))

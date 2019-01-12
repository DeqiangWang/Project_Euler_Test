# Euler 2


def iter_fib(stop):
    if stop < 3:
        return 3
    else:
        return iter_fib(prev_num0, prev_num1 + prev_num0, stop-1)


print(iter_fib())

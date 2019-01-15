# Euler 2


def fib_seq(limit):
    x = [1, 2];
    yield 1
    yield 2
    while x[-1] < limit:
        x.append(x[-2] + x[-1])
        if x[-1] <= limit:
            yield x[-1]
            

def array_evsum(self):
    even_arr_sum = 0
    for x in range(self.__len__()):
        if self[x]%2 == 0:
            even_arr_sum = even_arr_sum + self[x]
        else:
            pass
    return even_arr_sum
    
    
fibnum = list(fib_seq(4000000))
print(array_evsum(fibnum))

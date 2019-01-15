# Utility 1


def isprime(n):
    if (n == 2) | (n == 3):
        return True
    else:
        for x in range(3, n, 2):
            if (n % x) == 0:
                return False
    return True


def getprime(start, stop):
    primelist = []

    # checking if starting number is prime number with odd prime gap
    if start == 2:
        primelist.append(2)

    # increment of 2 for a prime start, reduce complexity
    if isprime(start) & start != 2:
        primelist.append(start)
        for x in range(start + 2, stop, 2):
            if isprime(x):
                primelist.append(x)

    # find the first prime after non prime start, then apply the same logic in second if block
    if not isprime(start):
        for i in range(start):
            if isprime(i):
                primelist.append(i)
                break
        for k in range(primelist[-1],stop,2):
            for l in range(start + 2, stop, 2):
                if isprime(x):
                    primelist.append(x)

    return primelist

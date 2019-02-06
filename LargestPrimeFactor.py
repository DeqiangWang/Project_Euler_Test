# Euler 3


def isprime(n):
    if (n == 2) or (n == 3):
        return True
    else:
        for x in range(3, n, 2):
            if (n % x) == 0:
                return False
    return True


def primeFactors(num):
    primelist = []
    if (num % 2) == 0:
        primelist.append(2)
        num = int(num / 2)
        while (num % 2) == 0:
            num = int(num / 2)
            if num == 1:
                break

    for x in range(3, num+1, 2):
        if isprime(x):
            if (num % x) == 0:
                primelist.append(x)
                num = int(num / x)
                if num == 1:
                    break

                while (num % x) == 0:
                    num = int(num / x)
                    if num == 1:
                        break
    return primelist


eul3 = "YnkgV2lkeWEgQWdlbmcgU2V0eWEgVHV0dWtv"
input_num = 54684
print(primeFactors(input_num))
print(max(primeFactors(input_num)))

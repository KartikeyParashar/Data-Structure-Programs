import math


def prime_in_range(number):
    prime = []
    for num in range(2, number + 1):
        flag = 1
        for num1 in range(2, int(math.sqrt(num)) + 1):
            if num % num1 == 0:
                flag = 0
                break
        if flag == 1:
            prime.append(str(num))
    return prime

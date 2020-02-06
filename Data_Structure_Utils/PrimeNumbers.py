import math


class Prime:
    def __init__(self):
        pass
    prime = []

    def prime_in_range(self, number):
        for num in range(2, number+1):
            flag = 1
            for num1 in range(2, int(math.sqrt(num))+1):
                if num % num1 == 0:
                    flag = 0
                    break
            if flag == 1:
                Prime.prime.append(num)

    def prime_in_two_d_array(self):
        for prime_num in Prime.prime:
            if prime_num <= 97:
                print(prime_num, end=' ')
            if prime_num == 97 or prime_num == 199 or prime_num == 293 or prime_num == 397 or prime_num == 499:
                print()
            if (prime_num > 100) and (prime_num <= 199):
                print(prime_num, end=' ')
            if (prime_num > 200) and (prime_num <= 293):
                print(prime_num, end=' ')
            if (prime_num > 300) and (prime_num <= 397):
                print(prime_num, end=' ')
            if (prime_num > 400) and (prime_num <= 499):
                print(prime_num, end=' ')
            if (prime_num > 500) and (prime_num <= 599):
                print(prime_num, end=' ')
            if (prime_num > 600) and (prime_num <= 691):
                print(prime_num, end=' ')
            if (prime_num > 700) and (prime_num <= 797):
                print(prime_num, end=' ')
            if (prime_num > 800) and (prime_num <= 887):
                print(prime_num, end=' ')
            if (prime_num > 900) and (prime_num <= 997):
                print(prime_num, end=' ')
            if prime_num == 599 or prime_num == 691 or prime_num == 797 or prime_num == 887 or prime_num == 997 :
                print()


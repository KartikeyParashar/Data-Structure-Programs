from Data_Structure_Utils.PrimeNumbers import Prime


def main():
    object_of_prime = Prime()
    object_of_prime.prime_in_range(1000)

    lower_limit = 0
    higher_limit = lower_limit + 100
    arr = []
    for i in range(1, 11):
        arr1 = []
        for num in object_of_prime.prime:
            if lower_limit < num < higher_limit:
                arr1.append(num)
        arr.append(arr1)
        lower_limit = higher_limit
        higher_limit = lower_limit + 100

    print(arr)


main()

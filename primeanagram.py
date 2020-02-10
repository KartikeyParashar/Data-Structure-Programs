from Data_Structure_Utils.prime_numbers_list import prime_in_range


def main():
    prime = prime_in_range(1000)
    prime_anagram = []
    prime_not_anagram = []
    for prime_num in prime:
        if prime_num[::-1] in prime:
            prime_anagram.append(int(prime_num))
        else:
            prime_not_anagram.append(int(prime_num))
    lower_limit = 0
    higher_limit = lower_limit + 100
    arr_anagram = []
    arr_not_anagram = []
    print("Prime Anagram numbers are :")
    for i in range(1, 11):
        arr = []
        for num in prime_anagram:
            if lower_limit < num < higher_limit:
                arr.append(num)
        arr_anagram.append(arr)
        lower_limit = higher_limit
        higher_limit = lower_limit + 100
    print(arr_anagram)

    lower_limit = 0
    higher_limit = lower_limit + 100
    print("\nPrime numbers which are not anagram are: ")
    for i in range(1, 11):
        arr = []
        for num in prime_not_anagram:
            if lower_limit < num < higher_limit:
                arr.append(num)
        arr_not_anagram.append(arr)
        lower_limit = higher_limit
        higher_limit = lower_limit + 100
    print(arr_not_anagram)


main()


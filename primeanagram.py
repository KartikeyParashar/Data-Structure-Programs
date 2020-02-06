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
    print("Prime Anagram numbers are is :")
    print(prime_anagram)

    print("\nPrime numbers which are not anagram are: ")
    print(prime_not_anagram)


main()


from Data_Structure_Utils.linked_list import Linked_List
from Data_Structure_Utils.prime_numbers_list import prime
from Data_Structure_Utils.prime_numbers_list import prime_in_range


def main():
    prime_in_range(1000)
    obj_of_ll = Linked_List()

    prime_anagram = []

    for num in prime:
        if num[::-1] in prime:
            prime_anagram.append(num)

    for num in range(len(prime_anagram)-1,0,-1):
        print(prime_anagram[num], end=' ')


main()


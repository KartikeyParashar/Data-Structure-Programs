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
    print("Prime Anagram numbers are :")
    for num in prime_anagram:
        if lower_limit < num < higher_limit:
            print(num,end = ' ')
        lower_limit = 0
    higher_limit = lower_limit + 100else : 
            print()
            print(num,end=' ')
            lower_limit = higher_limit
            higher_limit = lower_limit + 100
            while num not in range(lower_limit,higher_limit+1):
                lower_limit = higher_limit
                higher_limit = lower_limit + 100
                
   
    lower_limit = 0
    higher_limit = lower_limit + 100            
    print("\nPrime numbers which are not anagram are: ")
    for num in prime_not_anagram:
        if lower_limit < num < higher_limit:
            print(num,end = ' ')
        else : 
            print()
            print(num,end=' ')
            lower_limit = higher_limit
            higher_limit = lower_limit + 100
            while num not in range(lower_limit,higher_limit+1):
                lower_limit = higher_limit
                higher_limit = lower_limit + 100

                
main()

from Data_Structure_Utils.linked_list import Linked_List
from Data_Structure_Utils.prime_numbers_list import prime
from Data_Structure_Utils.prime_numbers_list import prime_in_range


def main():
    prime_in_range(1000)
    obj_of_ll = Linked_List()

    for num in prime:
        if num[::-1] in prime:
            obj_of_ll.insert_at_start(num)

    obj_of_ll.traverse()
    for num in obj_of_ll.elements:
        print(num, end=" ")

        
main()        



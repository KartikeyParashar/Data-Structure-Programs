from Data_Structure_Utils.prime_numbers_list import prime_in_range
from Data_Structure_Utils.prime_numbers_list import prime
from Data_Structure_Utils.linked_list import Linked_List


obj_of_ll = Linked_List()
prime_in_range(1000)




for number in prime:
    if number[::-1] in prime:
        obj_of_ll.insert_at_end(number)

obj_of_ll.traverse()
for num in obj_of_ll.elements:
    print(num, end=' ')

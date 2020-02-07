from Data_Structure_Utils.prime_numbers_list import prime_in_range
from Data_Structure_Utils.prime_numbers_list import prime
from Data_Structure_Utils.linked_list import Linked_List


obj_of_ll = Linked_List()
prime_in_range(1000)

for num in prime:
    obj_of_ll.insert_at_end(num)

obj_of_ll.traverse()
for number in obj_of_ll.elements:
    if number[::-1] in obj_of_ll.elements:
        print(number, end=' ')

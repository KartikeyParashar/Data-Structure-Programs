# Desc ­> Read .a List of Numbers from a file and arrange it ascending Order in a
# Linked List. Take user input for a number, if found then pop the number out of the
# list else insert the number in appropriate position
# b. I/P ­> Read from file the list of Numbers and take user input for a new number
# c. Logic ­> Create a Ordered Linked List having Numbers in ascending order.
# d. O/P ­> The List of Numbers to a File.

from Data_Structure_Utils.linked_list import Linked_List


linked_list = Linked_List()

def main1():
    file_1 = open("file.txt",'r')
    lines_of_file = file_1.readlines()
    # Traversing all the words in file
    for single_line in lines_of_file:
        words = single_line.lower().split()
        for word in words:
            linked_list.insert_at_end(word)

    return linked_list.traverse()

def main2():
    # Searching the word from given file
    print()
    search = input("Enter the element you want to search: ")
    if linked_list.search(search):
        linked_list.delete(search)
        Linked_List.elements.remove(search)
        print(f"Word {search} is in the Linked list of files and its now deleted")
        return  linked_list.sort()

    else:
        linked_list.insert_at_end(search)
        Linked_List.elements.append(search)
        linked_list.sort()
        print(f"Word {search} not present in Linked List and hence added")
        return linked_list.sort()

def main():
    print("Before sorting: ")
    for i in main1():
        print(i,end=" ")
    print()

    print("After sorting: ")
    for i in linked_list.sort():
        print(i,end=' ')
    print()

    for i in main2():
        print(i,end=" ")

main()
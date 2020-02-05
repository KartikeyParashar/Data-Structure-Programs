# Desc ­> Read the Text from a file, split it into words and arrange it as Linked List.
# Take a user input to search a Word in the List. If the Word is not found then add it
# to the list, and if it found then remove the word from the List. In the end save the
# list into a file
# I/P ­> Read from file the list of Words and take user input to search a Text
# Logic ­> Create a Unordered Linked List. The Basic Building Block is the Node
# Object. Each node object must hold at least two pieces of information. One ref to
# the data field and second the ref to the next node object.
# O/P ­> The List of Words to a File.

from Data_Structure_Utils.linked_list import *


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
        print()
        print(f"Word {search} is in the Linked list of files and its now deleted")
        print()
    else:
        print()
        print(f"Word {search} not present in Linked List and hence added")
        print()
        linked_list.insert_at_end(search)
    return linked_list.add_the_words()

for word in main1():
    print(word,end = " ")
print(main2())



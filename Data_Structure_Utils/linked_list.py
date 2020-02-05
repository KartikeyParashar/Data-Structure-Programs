class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.root = None

    elements = []
    def insert_at_end(self,value):
        newnode = Node(value)
        if self.root == None:
            self.root = newnode
        else:
            temp = self.root
            while temp.next!=None:
                temp = temp.next
            temp.next = newnode

    def insert_at_start(self,value):
        newnode = Node(value)
        if self.root == None:
            self.root = newnode
        else:
            newnode.next = self.root
            self.root = newnode

    def insert_after_item(self,value):

        newnode = Node(value)
        temp = self.root
        if self.root == None:
            self.root = newnode
        while True:
            pos = int(input("Enter the position after which you want to insert: "))

            if(pos >= Linked_List.length(self)):
                print("Please Enter a valid position")
            else:
                while pos-1:
                    temp = temp.next
                    pos-=1

            newnode.next = temp.next
            temp.next = newnode
            break

    def insert_before_item(self,value):
        newnode = Node(value)
        temp = self.root

        while True:
            pos = int(input("Enter the position before which you want to insert: "))

            if pos > Linked_List.length(self):
                print("Please Enter a valid position")
            else:
                while pos-2:
                    temp = temp.next
                    pos-=1
            newnode.next =temp.next
            temp.next = newnode
            break


    def traverse(self):
        temp = self.root
        if self.root == None:
            print("Nothing to Traverse")
        else:
             while temp is not None:
                # print(temp.data,end=' ')
                Linked_List.elements.append(temp.data)
                temp=temp.next
        return Linked_List.elements
    def length(self):
        len = 0
        temp = self.root
        while temp is not None:
            temp = temp.next
            len+=1
        return len

    def search(self,ele):
        if self.root == None:
            print("Nothing is present in list to Search")
        else:
            temp = self.root
            while temp is not None:
                if temp.data == ele:
                    return True
                temp = temp.next
            print("Item Not Found")
            return False

    def delete(self,value):
        if self.root == None:
            print("Nothing is present in list to delete")
        else:
            if self.root.data == value:
                self.root = self.root.next
            else:
                temp1 = self.root
                temp = self.root.next
                while temp is not None:
                    if temp.data == value:
                        temp1.next = temp.next
                        break
                    temp1 = temp1.next
                    temp = temp.next
                if temp is None:
                     print("Element not found")

    def add_the_words(self):
        temp = self.root
        temp_string = ""
        while temp:
            temp_string = temp_string + temp.data + " "
            temp = temp.next
        return temp_string

    def sort(self):
        return sorted(Linked_List.elements)


# a = Linked_List()
# while True:
#     print("linked List have following operations: ")
#     print("1.Insert at End")
#     print("2.Insert at Start")
#     print("3.Insert after")
#     print("4.Insert Before")
#     print("5.Length of List")
#     print("6.Traverse the list")
#     print("7.Search an element")
#     print("8.Delete an element")
#     print("9.Sorting")
#     print("10.Exit")
#
#     choice = int(input("Enter the choice(1-7)"))
#     if choice == 1:
#         ele = int(input("Enter the element you want to insert: "))
#         a.insert_at_end(ele)
#
#     elif choice == 2:
#         ele = int(input("Enter the element you want to insert: "))
#         a.insert_at_start(ele)
#
#     elif choice == 3:
#         ele = int(input("Enter the element you want to insert: "))
#         a.insert_after_item(ele)
#
#     elif choice == 4:
#         ele = int(input("Enter the element you want to insert: "))
#         a.insert_before_item(ele)
#
#     elif choice == 5:
#         print(f"The length of list is {a.length()}")
#
#     elif choice == 6:
#         print(a.traverse())
#
#     elif choice == 7:
#         ele = int(input("Enter the element you want to search: "))
#         print(a.search(ele))
#
#     elif choice == 8:
#         ele = int(input("Enter the element you want to delete: "))
#         a.delete(ele)
#
#     elif choice == 9:
#         print(a.sort())
#
#     elif choice == 10:
#         break
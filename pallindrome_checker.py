from Data_Structure_Utils.deque import Deque

def main():
    inputted_string = input("Enter the string you want to check that it is pallindrome or not: ")
    deque_object = Deque()
    return  deque_object.check_pallindrome_or_not(inputted_string)

main()
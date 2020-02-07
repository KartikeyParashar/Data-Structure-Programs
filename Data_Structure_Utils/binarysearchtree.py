class BinarySearchTree:
    def __init__(self):
        pass

    def factorial(self, n):
        fact = 1
        for number in range(1, n+1):
            fact *= number
        return fact

    # (2n)! / ((n + 1)! * n!)

    def catalanFormula(self, nodes):
        number_of_bin_search_tree = int(self.factorial(nodes*2)//self.factorial(nodes+1)*self.factorial(nodes))
        return number_of_bin_search_tree

    def binary_search_tree(self):
        testcases = int(input("Enter number of test cases: "))
        for i in range(testcases):
            nodes_input = int(input("Enter the number of nodes: "))
            print(f"Test case {i}")
            print(f"For {nodes_input} nodes, there are {self.catalanFormula(nodes_input)} BinarySearchTree Possible")
            print()

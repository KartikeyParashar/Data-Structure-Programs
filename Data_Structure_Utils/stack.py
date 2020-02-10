class Stack:
    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        return self.items[-1]

    def size_of_stack(self):
        return len(self.items)

    def check_parenthesis_balance(self, expression):
        open_parenthesis = "([{"
        close_parenthesis = ")]}"

        balance = True

        for bracket in expression:

            print(bracket)
            if bracket in "([{":
                self.push(bracket)
            elif bracket in close_parenthesis:
                self.pop()
                # if self.is_empty():
                #     balance = False
                #     break

        if self.is_empty():
            print(f"The inputted expression : {expression}  is balanced")
        else:
            print(f"The inputted expression : {expression} is not balanced")

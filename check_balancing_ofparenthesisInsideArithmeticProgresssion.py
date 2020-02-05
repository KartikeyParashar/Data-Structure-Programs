# Desc ­> Take an Arithmetic Expression such as
# (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
# performance of operations. Ensure parentheses must appear in a balanced fashion.
# I/P ­> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
# Logic ­> Write a Stack Class to push open parenthesis “(“ and pop closed
# parenthesis “)”. At the End of the Expression if the Stack is Empty then the
# Arithmetic Expression is Balanced. Stack Class Methods are Stack(), push(),
# pop(), peak(), isEmpty(), size()
# d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.

from Data_Structure_Utils.stack import Stack

object_of_class_Stack = Stack()

def main1():
    expression = input("Enter any Artithmetic Expression: ")
    object_of_class_Stack.check_parenthesis_balance(expression)

main1()
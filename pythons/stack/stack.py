__Author__ = "danny mcwaves"
"""
i learnt about stacks in the earlier version as a record activation container that holds the variables
during the invocation of a function. so when the function is invoked the, the stack stores all the
variables in the function and release them as long as their parent functions once the function is done

this stack class is just being designed as a prototype of the python stack.
it is a list that holds all the data of a function during the operation of a function and release them
if possible.
"""


class Stack:
    def __init__(self):
        self.__elements = []

    def __str__(self):
        if self.is_empty():
            return None
        return str(self.__elements)

    def is_empty(self):
        # check whether the list is empty or not
        return self.__elements.__len__() == 0

    def push(self, items):
        # to append a new element to the list
        self.__elements.append(items)

    def peek(self):
        # lets look at the last element in the list
        if self.is_empty():
            return 'EmptyList'
        return self.__elements[self.__elements.__len__() - 1]

    def pop(self):
        # this is supposed to remove the remove the last element in the list
        if self.is_empty():
            return "EmptyList"
        return self.__elements.pop()

    def duplicate(self, times):
        return times * self.__elements

    def __len__(self):
        # to return the length of all the elements in the list
        return self.__elements.__len__()
""" This module improves on the built-in Python stack operations """


class Stack():
    """ This object Implement chainable stack operations"""
    def __init__(self, stack=[]):
        """ 
        Object is initialized with an empty default stack called 'stack', 
        if no stack is specified 
        """
        self.stack = stack
    def pop(self):
        """ chainable pop() operation. Popping an empty stack has no effect """
        if self.stack != []:
            self.stack.pop()
        return self
    def append(self, element):
        """ chainable append() operation """
        self.stack.append(element)
        return self
    def list(self):
        """ Function returns the contents of the stack """
        return self.stack


if __name__ == "__main__":
    S = Stack() # create object with default empty stack 'stack'
    assert(S.stack == [])
    assert(S.list() == [])
    assert(S.pop().list() == []) # pop empty stack, get empty stack
    assert(S.append(1).append(2).append(3).list() == [1, 2, 3])
    assert(S.pop().pop().list() == [1])
    assert(S.pop().pop().pop().pop().pop().list() == [])
    assert(S.append(10).append(20).pop().append(30).list() == [10, 30])
    MY_STACK = [1, 2]
    T = Stack(MY_STACK)
    assert(T.stack == [1, 2])
    assert(T.list() == [1, 2])
    assert(MY_STACK == [1, 2])
    assert(T.append(10).append(20).list() == [1, 2, 10, 20])
    assert(T.pop().pop().pop().append(100).append(200).append(300).list() 
        == [1, 100, 200, 300])
    assert(MY_STACK == [1, 100, 200, 300])

# time: O(1) | space: O(1)

class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        return self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """

        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """

        return min(self.stack)

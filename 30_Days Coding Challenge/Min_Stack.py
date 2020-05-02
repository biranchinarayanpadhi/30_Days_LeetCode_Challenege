class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=float("inf")
        self.min_stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1],x))
        else:
            self.min_stack.append(x)
     


    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()
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
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
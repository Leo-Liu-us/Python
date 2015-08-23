class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._stack.append(x)
        #when _min_stack is empty or x is smaller than the top
        #push x into _min_stack
        if (not self._min_stack) or x <= self._min_stack[-1]:
            self._min_stack.append(x)
            print self._min_stack
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self._stack:
            return
        else:
            top = self._stack.pop()
            if top <= self._min_stack[-1]:
                self._min_stack.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        if self._stack:
            return self._stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self._min_stack:
            return self._min_stack[-1]
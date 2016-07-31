"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
Subscribe to see which companies asked this question
"""
 #其实最naive的方法就是使用两个list, A 用来顺序存元素, B用来将A中的元素排序

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.sorted_stack = list() 

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        left, right = 0, len(self.sorted_stack) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.sorted_stack[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1
        self.sorted_stack.insert(left, x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        left, right = 0, len(self.sorted_stack) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.sorted_stack[mid] == x:
                self.sorted_stack.pop(mid)
                return
            elif self.sorted_stack[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.sorted_stack[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#另外一种是使用一个list, 保存当前新进来的元素和list中最小值之间的差距, 所以既保留了元素, 也保留了最小值
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_num = 0 # 代表当前stack中的最小值

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack: # 如果一个新的元素过来, 而且栈为空, 那个更新当前元素为最小元素, 而且当前元素与栈中最小元素的差距为0
            self.stack.append(0)
            self.min_num = x
            return
        self.stack.append(x - self.min_num) # 否则向栈中压入当前元素和栈中已有元素最小值的差距
        if x < self.min_num: # 更新最小元素
            self.min_num = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x < 0:
            self.min_num = self.min_num - x
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] + self.min_num if self.stack[-1] > 0 else self.min_num

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_num


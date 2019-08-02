"""

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


"""
# 使用两个栈，辅助栈只用来存储越来越小的值，最后取最小值的时候就取辅助栈的最后一个元素
#  反正是抄来抄去

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.help = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if not self.help or x <= self.help[-1]:
            self.help.append(x)
        else:
            self.help.append(self.help[-1])


    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.help.pop()
            return self.data.pop()



    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.help:
            return self.help[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

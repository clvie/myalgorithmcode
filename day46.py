"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number

编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 将数字转为字符串
        n = str(n)
        # 初始化一个集合,利用集合进行去重处理，防止一直循环下去
        rq = set()
        # 开始进行逻辑
        while 1:
            # 需要转换为字符串，因为整型不可迭代
            n = str(sum(int(i)**2 for i in n))
            if n == '1':
                return True
            if n in rq:
                return False
            rq.add(n)

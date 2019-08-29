"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false


"""

# 常规思路不断除以2
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 需要判断等于0 和 负数的情况
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                return False
        return True

"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes


给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。


"""

# 只需要统计这个数的阶乘中有几个5即可
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 5:
            res += n // 5
            # 对于25以及更大的数，25//5=5，里面还有一个5
            n //= 5
        return res

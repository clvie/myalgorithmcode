"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

"""
# 思路：二分法查找
class Solution():
    def mySqrt(self, x):
        # 先将特殊情况考虑
        if x == 0 or x == 1:
            return x
        # 定一个左边界和一个右边界
        left = 1
        right = x // 2
        # 当右边界大于左边界的时候进行计算中位数然后中位数平方与输入的值进行比较
        while left < right:
            # 中点应该取为右中位数，取左中位数的时候会产生死循环
            mid = left + (right - left +1) // 2
            squr = mid * mid
            # 如果大，就把右边界缩小
            if squr > x:
                right = mid - 1
            # 如果小后者等，就将中位数赋值给左边界或者说将左边界增大
            else:
                left = mid
        return left

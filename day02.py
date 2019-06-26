"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
题目说明
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0

"""

# 解题思路：int函数会自动去0，所以不用考虑0出现再前面的情况
# 主要是有一个正负数的判断
class  Solution():
    def reverse(self, x):
        st = str(x)
        if st[0] == '-':
            rest = '-' + st[::-1].strip("-")
            answer = int(rest)
            if answer < (-2) ** 31:
                return 0
            return answer
        else:
            rest = st[::-1]
            answer = int(rest)
            if answer > (2 ** 31 - 1):
                return 0
            return answer

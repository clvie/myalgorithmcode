"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗

"""
# 解法一，将输入的数字转为字符串，然后字符串反转来操作，偷懒式做法
class Solution():
    def isPalindrome(self, x):
        st = str(x)
        st1 = st[::-1]
        if st == st1:
            return True
        else:
            return False
        
        

# 解法二，不使用字符串，直接利用数学计算
# 难点是如何使用循环语句来将数值反转
class Solution():
    def isPalindrome(self, x):
        if x < 0:
            return False
        # 采用临时变量作为判断循环终止的条件
        x1 = x
        palindrome = 0
        while x1 > 0:
            palindrome = palindrome * 10 + x1 % 10
            x1 = x1 // 10
        # 最后判断转换后的值与原来的值是否相等即可
        return x == palindrome

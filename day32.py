"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false


"""

# 两头同时并进，号称双指针
class Solution:
    def isPalindrome(self, s):
        a = 0
        b = len(s) - 1
        while a < b:
            # 使用.isalnum()判断该字符是否为数值或者字母
            while a < b and not s[a].isalnum():
                a += 1
            while a < b and not s[b].isalnum():
                b -= 1
            if s[a].upper() != s[b].upper():
                return False
            else:
                a += 1
                b -= 1
        return True

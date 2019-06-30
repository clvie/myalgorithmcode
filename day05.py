"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 

"""

#  利用min和max函数进行比较，找出字符串中ASCII对应的最小和最大的字符串，然后循环比较
#  这种解法时间复杂度应该时O(m*n)吧
class Solution():
    def longestCommonPrefix(self, s):
        # 判断是否为空
        if not s:
            return ""
        # 取最长字符串
        s1 = min(s)
        # 取最短字符换
        s2 = max(s)
        # 对最短最长字符中的元素进行循环对比
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        # 只有一个元素的时候返回s1
        return s1

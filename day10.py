"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


"""
# 解法一：使用字符串切片
class Solution():
    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
 # 最好成绩64ms，太耗时了


# 解法二：使用find这个内置函数，没技术含量
class Solution():
    def strStr(self, haystack, needle):
        return haystack.find(needle)
    
  

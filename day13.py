"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5


"""
# 直接调用库函数
class Solution():
    def lengthOfLastWord(self, s):
        # 使用split将字符串分割
        s = s.split()
        if not s:
            return 0
        return len(s[-1])

    
# 模仿java大佬写的
class Solution():
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        if end == -1:
            return 0
        # 真正的结尾
        while end >= 0 and s[end] == " ":
            end -= 1
        # 除去尾部空格后的结尾
        end1= end
        while end1 >= 0 and s[end1] != " ":
            end1 -= 1
        return end - end1

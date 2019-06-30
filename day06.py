"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""
# 写起来最快的一种思路，把正确的都替换掉，最后返回s == ""
# 这种做法时间复杂度空间复杂度较高，每一次都得三种方式循环一遍
class Solution():
    def isValid(self, s):
        while "{}" in s or "[]" in s or "()" in s:
            s = s.replace("{}", "")

            s = s.replace("[]", "")

            s = s.replace("()", "")
        return s == ""

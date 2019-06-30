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

    
    
    
    
# 重新找一种方式进行解决    
# 利用栈这种数据结构进行操作，降低时间复杂度和空间复杂度
# 将左括号压入栈中，左括号为键右括号为值进行匹配
# 这种做法币官方的好理解一些
class Solution():
    def isValid(self, s):
        stack = []
        dict1 = {'[':']', '{':'}', '(':')'}
        for i in range(len(s)):
            if stack and stack[-1] in dict1 and s[i] == dict1[stack[-1]]:
                # 如果正常匹配，将元素从栈中压出
                stack.pop()
            else:
                stack.append(s[i])
        # 如果正常匹配，最后栈中为空，所以not stack 会返回True，否则返回False
        return not stack

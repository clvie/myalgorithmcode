"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number

给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701


"""
# 26进制转十进制
# ord函数会将字符串转换ASCII码
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        n = len(s)
        for i in range(n):
            tmp = ord(s[i]) - 64
            # *表示乘号    ** 表示次方
            res += tmp*26**(n - 1 -i)
        return res

    
# 26进制转十进制
# ord函数会将字符串转换ASCII码
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 第二种思路
        res = 0
        tmp = 1
        for i in s[::-1]:
            res += (ord(i) - 64) * tmp
            tmp *= 26
        return res
        
    

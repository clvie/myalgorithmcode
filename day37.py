"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

"""
# 据说是将题目看成26进制的问题进行求解
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        tmp = ""
        while n:
            yushu = n % 26
            if yushu == 0:
                tmp = 'Z' + tmp
                n -= 26
            else:
                tmp = chr(yushu + 64) + tmp
            n //= 26

        return tmp

"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

"""
# 思路：补位相加

class Solution():
    def addBinary(self, a, b):
        # 判断a,b的长度，将长的置为a
        if len(a) < len(b):
            a, b = b, a
        # 用来接受结果并最终返回
        res = ""
        # 如果a,b 不等，用“0”补齐
        b = "0"*(len(a) - len(b)) + b
        # 求和结果标志位
        su = 0
        # 倒序循环
        for i in range(len(a)-1, -1, -1):
            ai = int(a[i])
            bi = int(b[i])
            # 同位之和取余 与上一次结果相加
            res = str((ai + bi + su)%2) +res
            # 同位元素相加等于2的记录结果与高一位元素之和相加，也就是进位
            su = (ai + bi + su)//2
        #判断最高位下一位之和是否为2，是就需要进1
        if su == 1:
            res = "1" + res
        return res

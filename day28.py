"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""

# 思路，根据题意一步步来
class Solution():
    def generate(self, numRows):
        # 先将三种特殊情况列举出来
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        else:
            # 从第三行开始进行加法操作
            res = self.generate(numRows - 1)
            tmp = [1]
            l = len(res[-1])
            for i in range(l - 1):
                mid = res[-1][i] + res[-1][i+1]
                tmp.append(mid)
            tmp.append(1)
            res.append(tmp)
            return res

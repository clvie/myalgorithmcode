"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？


"""
# 和上一题思路一样，只是只用返回相应的那一行数据即可
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        row = [1]
        for i in range(rowIndex):
            # tmp表示第一个元素
            tmp = [1]
            for j in range(len(row) - 1):
                tmp.append(row[j] + row[j+1])
            # 表示最后一个元素
            tmp.append(1)
            row = tmp

        return row

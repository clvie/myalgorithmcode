"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree


给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

"""

# 暴力穷举俗称递归
class Solution():
    def isSameTree(self, p, q):
        # 首先判空
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        # 然后采用递归的方式
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)



# 官方的迭代解法用的python库函数，表示没看懂

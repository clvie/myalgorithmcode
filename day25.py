"""

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。


"""
# 自底向上进行递归操作
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def isBalanced(self, root):
        self.flag = True
        def panduan(root):
            if not root:
                return 0
            left = panduan(root.left) + 1
            right = panduan(root.right) + 1
            if abs(right - left) > 1:
                self.flag = False
            return max(left, right)
        panduan(root)
        return self.flag

    
    # 还有一种自顶向下的操作，这种题思路很简单，就是写代码比较烦，直接抄了

"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5


"""
# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 运行效率极差的一次
# 还是老思路，使用递归暴力解题
class Solution():
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        n = len(nums)
        mid = n // 2
      # 确定中间值，作为根节点
        root = TreeNode(nums[mid])
         # 确定左子节点
        root.left = self.sortedArrayToBST(nums[:mid])
          # 确定右子节点
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

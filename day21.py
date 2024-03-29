"""来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。


"""

# 造一棵和自己一模一样的树进行遍历
class Solution():
    def isSymmetric(self, root):
        return self.isMirror(root, root)
    def isMirror(self, leftRoot, rightRoot):
        if leftRoot == None and rightRoot == None:
            return True
        if leftRoot == None or rightRoot == None:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)

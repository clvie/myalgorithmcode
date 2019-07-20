"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]


"""
class Solution():
    def levelOrderBottom(self, root):
        # 结果列表
        queue = []
        # 接下来要循环的当前层节点，存的是节点
        cur = [root]
        while cur:
            # 初始化当前层结果列表为空，存的是val
            cur_layer_val = []
            # 初始化下一层结点列表为空
            next_layer_node = []

            for node in cur:
                if node:
                    # 将该结点的值加入当前层结果列表的末尾
                    cur_layer_val.append(node.val)
                    # 将该结点的左右孩子结点加入到下一层结点列表
                    next_layer_node.extend([node.left, node.right])
            if cur_layer_val:
                # 则把当前层结果列表插入到队列首端
                queue.insert(0, cur_layer_val)
            # 下一层的结点变成当前层，接着循环
            cur = next_layer_node
        # 返回结果队列
        return queue

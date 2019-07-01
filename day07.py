"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# 解法一：暴力递归,只理解思路
class Solution():
    def mergeTwoLists(self, l1, l2):
        # 先是判空
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        # 判断两个链表的头元素谁更小
        elif l1.val < l2.val:
            # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
        
        
# 时间复杂度O（m+n）    空间复杂度O（m+n）

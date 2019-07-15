"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

"""
class Solution():
    def deleteDuplicates(self, head):
        if head ==None or head.next ==None:
            return head
        p = head

        while True:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

            if p.next == None:
                break
        return head

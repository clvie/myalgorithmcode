"""

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]


"""

class Solution():
    def merge(self, nums1, m, nums2, n):
        # 记录nums1和nums2以及合并后的nums1的下标
        p1 = m - 1
        p2 = n - 1
        p = m + n -1
        # 倒着来，看谁最后一位大，就放在合并后的最后一位
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            # 合并后的nums1往前走一位
            p -= 1
        # 不懂
        nums1[:p2 + 1] = nums2[:p2 + 1]

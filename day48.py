"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false



"""

# 使用传说中的哈希散列表，也就是字典进行值的存储
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 初始化一个字典
        dict1 = {}
        for i, n in enumerate(nums):
            if n in dict1 and i - dict1[n] <= k:
                return True
            dict1[n] = i
        return False

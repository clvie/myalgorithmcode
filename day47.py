"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true


"""

# 使用集合去重，号称哈希表，相当于使用了内置算法，并不是很好
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set()
        for i in nums:
            if i in set1:
                return True

            set1.add(i)
        return False

    
    # 先使用sort函数进行排序，然后再寻找重复数字，同样使用了内置函数
    class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        if not nums:
            return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

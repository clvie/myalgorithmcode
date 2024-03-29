"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""

# 动态规划思想
class Solution():
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            # 该项与前面最大子序和的和，如果前面小于0就重新计算
            nums[i] = nums[i] + max(nums[i -1], 0)
        return max(nums)
    
# 对动态规划不熟悉，搞了半天才明白

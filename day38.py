"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2


"""
import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用库函数进行计数，值为键，次数为值，组成字典
        counts = collections.Counter(nums)
        # 传入命名参数key，其为一个函数，用来指定取最大值的方法,即通过counts.get的方法找最大值
        return max(counts.keys(), key = counts.get)

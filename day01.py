"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 ：整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
# 解答一
class TwoSum():
    """
    基本思路：利用枚举将下标求出，以数值为键，以下标为值存储在字典中
    通过循环将结果存放在列表中，返回


    利用字典有一个缺点，键不能重复，所以限制了列表中不能有重复的数值
    下面的代码虽然实现了基本思路，但是对于有重复数值的只能返回该数值最大的下标
    """

    def add_two_num(self, nums, target):
        dict1 = {}
        list1 = []
        for index, num in enumerate(nums):
            other_num = target - num
            dict1[num] = index
            if other_num in dict1:
                list1.append([dict1[other_num], index])

        return list1
        
        
        
        
        
# 解答二
def add_two_num(nums, target):
    """
    该方法把所有的情况都列举出来了 
    """
    list1 = []
    for index1, num in enumerate(nums):
        other_num = target - num
        if other_num in nums:
            index2 = nums.index(other_num)

            list1.append([index1, index2])

    return list1



# 更好的办法还在探索中

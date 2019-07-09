"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""
# 解法一：倒着切片
# 思路：如果末尾数为9 就置为0
#      如果不为9 ，就正常加一
#      如果一直为9 就首位为1 加一个0
class Solution():
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[-(1+i)] == 9:
                digits[-(1+i)] = 0
                if -(1+i) == -len(digits):
                    digits[0] = 1
                    digits.append(0)
                    return digits
            else:
                digits[-(1+i)] += 1
                return digits
            
            
            
# 解法二：优化
class Solution():
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits

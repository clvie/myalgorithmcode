"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


"""
# 先排序后比较,但是效果不理想，比较耗时
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        if s != t:
            return False
        return True
    
   # 找到了一种比较高效的解法，利用字典这种容器进行计数，运行结果确实比sorted函数快
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # 使用字典的解法
        # 使用defaultdict是因为该函数可以当key不存在的时候不报错而返回一个默认值
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        # 使用两个字典进行计数
        for i in s:
            dict1[i] += 1

        for j in t:
            dict2[j] += 1

        if len(dict1) != len(dict2):
            return False
        else:
            for n in dict1:
                if dict1[n] != dict2.get(n):
                    return False
        return True
    
    
    
    
    
# efaultdict接受一个工厂函数作为参数，如下来构造：
# dict =defaultdict( factory_function)
#
# 这个factory_function可以是list、set、str等等，作用是当key不存在时，
# 返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0
# 例如：
from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] ='two'

print(dict1[1])
print(dict2[1])
print(dict3[1])
print(dict4[1])

#结果：
0
set()

[]

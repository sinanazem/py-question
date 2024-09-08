class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict_={}
        i = 0
        while i < len(nums):
            
            if nums[i] in dict_:
                
                return [i, dict_[nums[i]]]
            
            else:
                val = target - nums[i]
                dict_[val]=i
            
            i+=1
            
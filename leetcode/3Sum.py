class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        length = len(nums)
        
        for i in range(length-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, length-1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1 
                    right -= 1
                
                elif current < 0:
                    left += 1
                
                else:
                    right -= 1
        return output
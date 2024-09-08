class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        lst, quad = [], []
        
        def ksum(k, start, target):
            if k != 2:
                for i in range(start, len(nums)-k +1):
                    quad.append(nums[i])
                    ksum(k-1, i+1, target-nums[i])
                    quad.pop()
                    return 
            l, r = start, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l+=1
                    
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    lst.append(quad + nums[r]+nums[l])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
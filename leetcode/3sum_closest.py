class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float("-inf")
        length = len(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, length-1
            
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == target:
                    return target
                if abs(cur-target) < abs(closest-target):
                    closest = cur
                elif cur < target:
                    left+=1
                else:
                    right-=1
            
        return closest






        
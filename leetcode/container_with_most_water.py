class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right = (0, len(height) - 1)
        res = 0
        m = max(height)

        while left < right:
            a = (right - left)*(min(height[left], height[right]))
            if a > res:
                res = a
            if  height[left] < height[right]:
                left+=1
            else:
                right-=1

            if res > m*(right-left):
                break
        return res

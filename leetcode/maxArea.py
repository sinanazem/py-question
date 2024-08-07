def maxArea(height):
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

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
    
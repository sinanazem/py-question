class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign, x = (1, x) if x >= 0 else (-1, -x)
        res = 0
        while x>0:
            res = res*10 + x%10
            x//=10
        
        res*= sign

        if res <= -2**31-1 or res >= 2**31:

            return 0
        
        else:
            return res
        
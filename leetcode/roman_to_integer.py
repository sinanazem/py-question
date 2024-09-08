class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        symbols = {
            'M':1000, 
            'CM':900, 
            'D':500, 
            'CD':400, 
            'C':100, 
            'XC':90, 
            'L':50, 
            'XL':40, 
            'X':10, 
            'IX':9, 
            'V':5, 
            'IV':4, 
            'I':1
        }

        res = 0

        for i in range(len(s)-1):
            if symbols[s[i]] < symbols[s[i+1]]:
                res -= symbols[s[i]]
            else:
                res += symbols[s[i]]

        res += symbols[s[-1]]
        return res




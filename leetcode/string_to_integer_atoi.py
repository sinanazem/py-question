class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.lstrip()
        length = len(s)
        i = 0
        
        sign = 1
        if not length:
            return 0
            
        if s[0] == "+":
            sign = 1
            i+=1
        
        elif s[0] == "-":
            sign = -1
            i+=1

        res = 0
        while i < length:
            if not s[i].isdigit():
                break
            else:
                res = res*10 + int(s[i])
            i += 1
        
        
        res*= sign
        
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        else:
            return res
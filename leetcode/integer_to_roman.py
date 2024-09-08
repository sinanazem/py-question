class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = [
            (1000, 'M'), 
            (900, 'CM'), 
            (500, 'D'), 
            (400, 'CD'), 
            (100, 'C'), 
            (90, 'XC'), 
            (50, 'L'), 
            (40, 'XL'), 
            (10, 'X'), 
            (9, 'IX'), 
            (5, 'V'), 
            (4, 'IV'), 
            (1, 'I')
        ]
                    
        res = ""
    
        for k, v in symbols:
            c = num // k 
            if c:
                res += c * v
                num %= k
                if num == 0:
                    break
        return res
class Solution(object):
    def isMatch(self, s, p):
        memo = {}
        
        def dts(sp, pp):
            if (sp, pp) in memo:
                return memo[(sp, pp)]
            
            if sp >= len(s) and pp >= len(p):
                return True
            
            if pp >= len(p):
                return False
            
            match = sp < len(s) and (s[sp] == p[pp] or p[pp] == ".")
            
            if pp+1 < len(p) and p[pp+1] == "*":
                memo[(sp, pp)] = dts(sp, pp+2) or (match and dts(sp+1, pp))
                return memo[(sp, pp)]
            
            if match:
                memo[(sp, pp)] = dts(sp+1, pp+1)
                return memo[(sp, pp)]
            
            memo[(sp, pp)] = False
            return False

        return dts(0, 0)

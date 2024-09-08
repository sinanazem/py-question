class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ""
        res_length = 0

        for i in range(n):
            # odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res = s[l:r+1]
                    res_length = (r - l + 1)
                
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res = s[l:r+1]
                    res_length = (r - l + 1)
                
                l -= 1
                r += 1
        return res
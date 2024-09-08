class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_ = set()
        i = j = 0
        length, max_ = (len(s), 0) if len(s) else (0, 0)

        while j < length:
            if s[j] not in set_:
                set_.add(s[j])
                
                if max_ <= j-i:
                    max_ = j-i+1
                
                j += 1

            else:
                set_.remove(s[i])
                i += 1
        
        return max_
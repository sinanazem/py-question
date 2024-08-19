class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dict_= {
            "(":")",
            "{":"}",
            "[":"]"
            }
        stack = []
        
        for i in s:
            if i in dict_:
                stack.append(i)

            elif len(stack) == 0 or  i != dict_[stack[-1]]:
                return False
            else:
                stack.pop()
        
        if len(stack):
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.isValid("({)")
    print(result)
    
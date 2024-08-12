class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        lst = []

        def backtracker(i, current_str):
            
            if len(current_str) == len(digits):
                lst.append(current_str)
                return
        
            for c in letters[digits[i]]:
                backtracker(i+1, current_str+c)
        
        if len(digits):
            backtracker(0, "")
        return lst


if __name__ == "__main__":
    digits = "23"
    solution = Solution()
    result = solution.letterCombinations(digits)
    print(result)
    
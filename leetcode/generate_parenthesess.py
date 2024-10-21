class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack, lst = [], []
        
        def backtracker(op, cp):
            
            if op == cp == n:
                lst.append("".join(stack))
                return
            
            if op < n:
                stack.append("(")
                backtracker(op+1, cp)
                stack.pop()
                
            if cp < op:
                stack.append(")")
                backtracker(op, cp+1)
                stack.pop()
            
        backtracker(0, 0)
        return lst


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
        
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        flag = True
        row = 0
        m = [[] for i in range(numRows)]

        for ch in s:
            if flag:
                m[row].append(ch)
                row += 1
            else:
                row -= 1
                m[row].append(ch)
            
            if row == numRows:
                flag = not flag
                row -= 1
            
            elif row == 0:
                flag = not flag
                row += 1
        
        return "".join(["".join(lst) for lst in m])

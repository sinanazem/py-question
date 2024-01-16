class Solution(object):
    def isPalindrome(self, x):
        o_x = x
        r_x = 0
        while x > 0:
            r_x = r_x * 10 + (x % 10)
            x//= 10

        return r_x == o_x

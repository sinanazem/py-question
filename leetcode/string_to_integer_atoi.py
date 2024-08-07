
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """

    s = s.lstrip()
    n = len(s)
    if not n:
        return 0
    
    i = 0
    sign = 1
    if s[i] == '+':
        i+=1
    elif s[i] == '-':
        sign = -1
        i+=1
    
    res = 0
    while i<n:
        cur = s[i]
        if not cur.isdigit():
            break
        else:
            res = res*10 + int(cur)
        i+=1
    res*= sign

    if res > 2**31-1:

        return 2**31-1
    elif res < -2**31:

        return -2**31
    else:
        return res

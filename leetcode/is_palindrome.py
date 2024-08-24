def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """


    number = x
    res = 0
    while number > 0:
        res = res*10 + number%10
        number//=10
    return x == res
    
    
if __name__ == "__main__":
    print(isPalindrome(121))
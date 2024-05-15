class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = 0
        x_initial = x
        while x > 0:
            digit = x % 10
            x = x // 10
            reversed_x = reversed_x * 10 + digit
        if x_initial == reversed_x:
            return True
        else:
            return False
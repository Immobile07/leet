# Last updated: 9/13/2025, 4:23:21 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        z=str(x)
        y=z[::-1]
        for i in range(len(z)):
            if z[i]!=y[i]:
                return False
        else:
            return True
# Last updated: 4/4/2026, 12:41:48 AM
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        tmp=4
        if n==1:
            return True
        else:
            while(True):
                if tmp==n:
                    return True
                if tmp<n:
                    tmp*=4
                else:
                    return False
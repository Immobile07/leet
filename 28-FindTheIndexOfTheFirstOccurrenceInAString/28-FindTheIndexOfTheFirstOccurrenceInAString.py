# Last updated: 9/27/2025, 11:23:53 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cntr=None
        strt=None
        if haystack==needle:
            return 0
        elif len(needle)==1:
            for i in range(len(haystack)):
                if haystack[i]==needle:
                    return i
        for i in range(len(haystack)):
            if i+len(needle)<=len(haystack):
                if needle[:]==haystack[i:i+len(needle)]:
                    return i
        return -1
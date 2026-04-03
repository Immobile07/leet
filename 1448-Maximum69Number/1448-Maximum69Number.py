# Last updated: 4/4/2026, 12:41:25 AM
class Solution:
    def maximum69Number (self, num: int) -> int:
        num2=str(num)
        num3=[]
        for i in range(len(num2)):
            num3.append(num2[i])
        for i in range(len(num3)):
            if num3[i]=='6':
                num3[i]='9'
                break
        num2=''
        for i in range(len(num3)):
            num2+=num3[i]
        return int(num2)
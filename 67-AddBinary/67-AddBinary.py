# Last updated: 4/4/2026, 12:42:42 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        plc=len(a)
        place=plc-1
        a_dec=0
        for i in a:
            a_dec+=(int(i))*(2**place)
            place-=1
        plc_b=len(b)
        place_b=plc_b-1
        b_dec=0
        for j in b:
            b_dec+=int(j)*(2**place_b)
            place_b-=1
        conv=a_dec+b_dec
        lr=[]
        rem=-1
        while (rem!=0):
            lr.append(str(conv%2))
            conv=conv//2
            rem=conv
        return "".join(lr[::-1])
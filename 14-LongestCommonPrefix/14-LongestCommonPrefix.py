# Last updated: 4/15/2026, 11:48:33 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        lr=strs[0]
4        ln=len(strs)
5        for i in range(1,ln):
6            nw=strs[i]
7            if len(nw)>len(lr):
8                nw1=""
9                ln2=len(lr)
10                prev=True
11                for j in range(ln2):
12                    if nw[j]==lr[j] and prev==True:
13                        nw1+=lr[j]
14                    else:
15                        prev=False
16                lr=nw1
17            else:
18                nw1=""
19                ln2=len(nw)
20                prev=True
21                for j in range(ln2):
22                    if nw[j]==lr[j] and prev==True:
23                        nw1+=lr[j]
24                    else:
25                        prev=False
26                lr=nw1
27        return lr
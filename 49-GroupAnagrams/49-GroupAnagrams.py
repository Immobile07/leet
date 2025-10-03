# Last updated: 10/3/2025, 11:49:30 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ant=[]
        ln=len(strs)
        lst=[]
        for i in range(ln):
            b=sorted(strs[i])
            ant.append("".join(b))
            lst.append(False)
        check=[]
        frst=False
        cnt=0
        for i in range(ln):
            if lst[i]==False:
                check.append([strs[i]])
                lst[i]=True
                if frst!=False:
                    cnt+=1
                else:
                    frst=True
                for j in range(ln):
                    if i==j:
                        continue
                    else:
                        if ant[i]==ant[j] and lst[j]==False:
                            check[cnt].append(strs[j])
                            lst[j]=True
                        else:
                            continue
            else:
                continue
        return check
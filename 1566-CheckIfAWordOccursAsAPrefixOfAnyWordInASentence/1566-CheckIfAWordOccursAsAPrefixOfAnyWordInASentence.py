# Last updated: 4/4/2026, 12:41:23 AM
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sr=""
        wrd=[]
        for i in range(len(sentence)):
            if i==len(sentence)-1:
                sr+=sentence[i]
                wrd.append(sr)
            elif sentence[i]==" ":
                wrd.append(sr)
                sr=""
            else:
                sr+=sentence[i]
        for i in range(len(wrd)):
            nw=wrd[i]
            strt=0
            
            if wrd[i][0:len(searchWord)]==searchWord:
                return i+1
                break
            else:
                strt+=1
        return -1
        
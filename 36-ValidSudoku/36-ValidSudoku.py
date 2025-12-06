# Last updated: 12/7/2025, 1:14:41 AM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ln=len(board)
        # check columns
        for i in range(ln):
            check={}
            for j in range(ln):
                if board[i][j] in check.keys() and board[i][j]!='.':
                    return False
                else: 
                    check[board[i][j]]=True
        # check rows
        for i in range(ln):
            check={}
            for j in range(ln):
                if board[j][i] in check.keys() and board[j][i]!='.':
                    return False
                else: 
                    check[board[j][i]]=True
        # check the 3x3
        checked=0
        eachthree=0
        eachthree2=0
        st=0
        tile_dn=0
        while (eachthree<=8):
            dct={}
            for i in range(st,st+3):
                
                for j in range(eachthree2,eachthree2+3):
                    if board[i][j] in dct.keys() and board[i][j]!='.':
                        return False
                    else:
                        dct[board[i][j]]=True
        
            eachthree+=1
            eachthree2+=3
            if eachthree%3==0:
                st+=3
                eachthree2=0
        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = [0]*9
        for row in board:
            for i in range (9):
                if row[i]!=".":
                    val = int(row[i])        
                    if count[val -1] == 1: #-1 to translate from 1-9 to 0-8
                        # we found a duplicate
                        return False
                    else: count[val -1] = 1  
            # reset count
            count = [0]*9
        for i in range (9):
            for j in range (9):
                if board[j][i]!=".":
                    val = int (board[j][i])
                    if count[val -1] == 1:
                        return False
                    else: count[val-1] = 1
            count = [0]*9
        for i in range (3):
            for j in range (3):
                for k in range (3*i, 3*(i+1)):
                    for l in range (3*j, 3*(j+1)):
                        if board[k][l]!=".":
                            val = int (board[k][l])
                            if count [val-1] == 1:
                                return False
                            else: count[val-1] = 1
                count =[0]*9
        return True
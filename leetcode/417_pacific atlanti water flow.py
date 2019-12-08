class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0: return []
        r_border = len(matrix)
        c_border = len(matrix[0])
        
        def helperP(row,col,resP,matP=None):
            
            if not matP: matP = set()
            if row <= 0 or col <= 0:
                return True
            
            try1 = try2 = try3 = try4 = False
            
            matP.add((row,col))
            
            if matrix[row][col] >= matrix[row-1][col] and (row-1,col) not in matP and (row-1,col) not in resP:
                try1 = helperP(row-1,col,resP,matP)
            if matrix[row][col] >= matrix[row][col-1] and (row,col-1) not in matP and (row,col-1) not in resP:
                try2 = helperP(row,col-1,resP,matP)
            if row+1 < r_border and matrix[row][col] >= matrix[row+1][col] and (row+1,col) not in matP and (row+1,col) not in resP:
                try3 = helperP(row+1,col,resP,matP)
            if col+1 < c_border and matrix[row][col] >= matrix[row][col+1] and (row,col+1) not in matP and (row,col+1) not in resP:
                try4 = helperP(row,col+1,resP,matP)

            
            return try1 or try2 or try3 or try4
        
        
        def helperA(row,col,resA,matA = None):
            if not matA: matA = set()
            if row >= r_border-1 or col >= c_border-1:
                return True
            try1 = try2 = try3 = try4 = False
            
            matA.add((row,col))
            
            if row+1 < r_border and matrix[row][col] >= matrix[row+1][col] and (row+1,col) not in matA and (row+1,col) not in resA:
                try1 = helperA(row+1,col,resA,matA)
            if col+1 < c_border and matrix[row][col] >= matrix[row][col+1] and (row,col+1) not in matA and (row,col+1) not in resA:
                try2 = helperA(row,col+1,resA,matA)
            if col-1 >= 0 and matrix[row][col] >= matrix[row][col-1] and (row,col-1) not in matA and (row,col-1) not in resA:
                try3 = helperA(row,col-1,resA,matA)
            if row-1 >= 0 and matrix[row][col] >= matrix[row-1][col] and (row-1,col) not in matA and (row-1,col) not in resA:
                try4 = helperA(row-1,col,resA,matA)

                
            return try1 or try2 or try3 or try4

        # print(helperP(2,1))
        res = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if helperP(i,j,res) and helperA(i,j,res):
                    res.add((i,j))
                    
        return res


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0: return []

        vis = set()
        visP = set()
        visA = set()

        if row == 0 or col == 0:
            visP.add((row,col))
        elif row == len(matrix) or col = len(matrix[0]):
            visA.add((row,col))

        
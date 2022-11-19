class Solution:
    # @param A : list of strings
    # @return an integer
    def mapcolor(B):
        if B == "r":
            return 0
        if B == "g":
            return 1
        if B == "b":
            return 2
    def solve(self, A):
        Col = len(A[0])
        Row = len(A)
        area = mapcolor(A[i][j])
        area = 0
        
        toprow = [[10000 for c in range(Col)] for r in range(3)]
        btmrow = [[-1 for c in range(Col)] for r in range(3)]
        left = [10000]*3
        right = [-1]*3
        for c in range(Col):
            for r in range(Row):
                btmrow[mapcolor(A[r][c])][c] = max(btmrow[mapcolor(A[r][c])][c],r)
                toprow[mapcolor(A[r][c])][c] = min(toprow[mapcolor(A[r][c])][c],r) 
                left[mapcolor(A[r][c])] = min(left[mapcolor(A[r][c])],c)
                right[mapcolor(A[r][c])] = max(right[mapcolor(A[r][c])],c)
        return maxarea(toprow,btmrow,left,right)
    
    def maxarea(toprow ,btmrow ,left , right):
        area = 0
        for c in range(Col):
            for col1 in range(3):
                for col2 in range(3):
                    if col1 != col2:
                        col3 = 3 - col2 - col1
                        if toprow[col1][col] != 10000 and btmrow[col2][col] != -1 and left[col3]!=10000:
                            area = max(area,0.5*(abs(toprow[col1][col]-btmrow[col2][col])+1)*(abs(left[col3]-col)+1))
                        if toprow[col1][col] != 10000 and btmrow[col2][col] != -1 and right[col3]!=-1:
                            area = max(area,0.5*(abs(toprow[col1][col]-btmrow[col2][col])+1)*(abs(right[col3]-col)+1))
        return area            
                
                                
                            
                                    
                                


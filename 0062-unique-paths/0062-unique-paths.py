class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat=[[0]*n for _ in range(m)]


        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1>=m and j+1>=n:
                    mat[i][j]=1
                elif i+1>=m:
                    mat[i][j]=mat[i][j+1]
                elif j+1>=n:
                    mat[i][j]=mat[i+1][j]
                else:
                    mat[i][j]=mat[i+1][j]+mat[i][j+1]
        # print(mat)
        return mat[0][0]

        
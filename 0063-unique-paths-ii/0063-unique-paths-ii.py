class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp={}
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        def f(n,m):
            if (n,m) in dp:
                return dp[(n,m)]
            
            if n<=0 or m<=0 :
                return 0
            if obstacleGrid[m-1][n-1]==1:
                return 0
            if n==1 and m==1:
                return 1
            
            
            dp[(n,m)]=f(n,m-1) +f(n-1,m)

            return dp[(n,m)]
        return f(n,m)
        
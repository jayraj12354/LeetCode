class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def f(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if i>=len(text1) or j>=len(text2):
                return 0
            if text1[i]==text2[j]:
                dp[(i,j)]= 1+f(i+1,j+1)
            else:
                dp[(i,j)]= max(f(i,j+1),f(i+1,j))
            
            return dp[(i,j)]
        return f(0,0)
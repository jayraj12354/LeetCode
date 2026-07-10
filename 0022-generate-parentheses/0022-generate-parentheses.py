class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr=[]
        def f(n,i,s):
            if i==2*n+1:
                r=0
                l=0
                for j in s:
                    if j=="(":
                        r+=1
                    if j==")":
                        l+=1
                    if l>r:
                        return 
                if l==r:
                    arr.append(s)
                return 
            f(n,i+1,s+"(")
            f(n,i+1,s+")")
        f(n,1,"")
        return arr
            


        
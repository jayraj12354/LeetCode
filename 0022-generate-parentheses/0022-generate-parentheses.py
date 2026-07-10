class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr=[]

        def f(n,i,s,l,r):
            if i==2*n and l==n and r==l:
                arr.append("".join(s))
                return 
            if r<n:
                s.append("(")
                f(n,i+1,s,l,r+1)
                s.pop()
            if l<r:
                s.append(")")
                f(n,i+1,s,l+1,r)
                s.pop()
        f(n,0,[],0,0)
        return arr
            


        
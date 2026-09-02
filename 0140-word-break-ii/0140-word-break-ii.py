class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans=[]
        arr=[]

        def f(i,s,c):

            if len(arr)>0 and arr[-1] in wordDict and c==len(s):
                    ans.append(" ".join(arr[::]))
                

            if i>=len(s):
                return

            if len(arr)==0  or (arr[-1] in wordDict):
                arr.append(s[i])
                f(i+1,s,c+1)
                arr.pop()

            if len(arr)>0:
                arr[-1]+=s[i]
                f(i+1,s,c+1)


        f(0,s,0)
        return ans

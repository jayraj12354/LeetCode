class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        copy=strs[0]
        j=0
        stop=False
        while True:
            for i in range(len(strs)):
                # print(strs[i],copy[j])
                if (not strs[i]) or (strs[i][0]!=copy[j]):
                    stop=True
                    break

                if len(strs[i])>1:
                    strs[i]=strs[i][1::]
                elif len(strs[i])==1:
                    strs[i]=""
            if stop:
                break
            ans+=copy[j]
            j+=1
            # print(strs)
        return ans
                
                
        
        
        
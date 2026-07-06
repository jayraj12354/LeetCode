class Solution:
    def romanToInt(self, s: str) -> int:
        arr=[[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
        i=len(s)-1
        ans=0
        while i>=0:
            if i>=1 and (s[i-1]+s[i] in ["CM","CD","XC","XL","IX","IV"]):
                for j in range(len(arr)):
                    if arr[j][1]==s[i-1]+s[i]:
                        ans+=arr[j][0]
                i-=2
            else:
                for j in range(len(arr)):
                    if arr[j][1]==s[i]:
                        ans+=arr[j][0]
                i-=1
        return ans
            
                    
                    


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # num=[str(i) for i in range(2,10)]
        num=["2","3","4","5","6","7","8","9"]
        val=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        arr=[]


        def f(digits,i,s):
            print(s)
            if i==len(digits):
                arr.append(s)
                return
            
            for j in val[int(digits[i])-2]:
                f(digits,i+1,s+j)

        f(digits,0,"")

        return arr

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if  stack :
                if (stack[-1]=="(" and i==")") or (stack[-1]=="[" and i=="]") or (stack[-1]=="{" and i=="}"):
                    stack.pop()
                    continue
            stack.append(i)

        return not stack


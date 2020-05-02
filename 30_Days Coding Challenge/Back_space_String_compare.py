class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack=[]
        length=len(S)
        res=""
        for i in range(length):
            if S[i] == "#" and len(stack)!=0:
                stack.pop()
            elif S[i]=="#" and len(stack)==0:
                continue
            else:
                stack.append(S[i])
                
        while len(stack)!=0:
            res+=stack.pop()
        
        length=len(T)
        res1=""

        for i in range(length):
            if T[i] == "#" and len(stack)!=0:
                stack.pop()
            elif T[i]=="#" and len(stack)==0:
                continue
            else:
                stack.append(T[i])
                
        while len(stack)!=0:
            res1+=stack.pop()
            
        print(res1,res)
        return res1==res
            
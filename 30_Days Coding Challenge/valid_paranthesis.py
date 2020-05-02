class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) == 1 and s[0] == "*":
            return True
        
        left_braces_stack=[]
        star_stack=[]
        length=len(s)
        for i in range(length):
            if s[i] == "(":
                left_braces_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if len(left_braces_stack) != 0:
                    left_braces_stack.pop()
                elif len(star_stack) !=0:
                    star_stack.pop()
                else:
                    return False
                
        while len(left_braces_stack) != 0:
            if len(star_stack) == 0 or star_stack.pop()<left_braces_stack.pop():
                return False
            
        return True
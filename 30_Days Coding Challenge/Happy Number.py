class Solution:
    def isHappy(self, a):
        number_generated=[]
        value=a
        while value!=1:
            value=sum(int(i)**2 for i in str(value))
            if value in number_generated:
                return False
            else:
                number_generated.append(value)
        return True
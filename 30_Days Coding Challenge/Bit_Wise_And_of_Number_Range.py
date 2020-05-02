class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=""
        m=bin(m).replace("0b", "")
        n=bin(n).replace("0b", "")
        length_m=len(m)
        length_n=len(n)
        diff=length_m-length_n
        if diff < 0 :
            while diff!=0:
                m="0"+m
                diff+=1
            for i in range(length_m):
                if m[i]==n[i]:
                    res+=m[i]
                else:
                    current=i
                    while current<length_m:
                        res+="0"
                        current+=1
                    break
            print(res)
            return int(res,2)
     
        else:
            while diff!=0:
                n="0"+n
                diff-=1
            for i in range(length_m):
                if m[i]==n[i]:
                    res+=m[i]
                else:
                    current=i
                    while current<length_m:
                        res+="0"
                        current+=1
                    break
            return int(res,2)
     
         
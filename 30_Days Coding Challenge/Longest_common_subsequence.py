class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int

        """
        """"
        #Recusrion Problem without Memoization
        
        len1=len(text1)
        len2=len(text2)
        return self.LCS(text1,text2,0,0,len1,len2)
    
    def LCS(self,text1,text2,i,j,len1,len2):
        if i==len1 or j==len2:
            return 0
        elif text1[i]==text2[j]:
            return 1+self.LCS(text1,text2,i+1,j+1,len1,len2)
        else:
            return max(self.LCS(text1,text2,i+1,j,len1,len2),self.LCS(text1,text2,i,j+1,len1,len2))
        
        """
        text1=' '+text1
        text2=' '+text2
        len1=len(text1)
        len2=len(text2)
        mem=[[0 for j in range(len2)] for i in range(len1)]
    
        for i in range(1,len1):
            for j in range(1,len2):
                    if text1[i] == text2[j]:
                        mem[i][j]=1+mem[i-1][j-1]
                    else:
                        mem[i][j]=max(mem[i-1][j],mem[i][j-1])        
        return mem[-1][-1]
        
        
        
        
        
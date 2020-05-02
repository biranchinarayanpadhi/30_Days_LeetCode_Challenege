class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        dicti={}
        maxi=0
        length=len(nums)
        dicti[0]=-1
        for i in range(length):
            
            if nums[i] == 0:
                count-=1
                
            elif nums[i] == 1:
                count+=1
            
            if count in dicti:
                maxi=max(maxi,i-dicti[count])
            else:
                dicti[count]=i
        return maxi
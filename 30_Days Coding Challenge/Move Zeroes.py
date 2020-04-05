class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        length=len(nums)
        if length==1:
            return nums
        while j<=length-1:
            if nums[i]!=0:
                i+=1
            elif nums[j]!=0:
                nums[i]=nums[j]
                nums[j]=0
                i+=1
            j+=1

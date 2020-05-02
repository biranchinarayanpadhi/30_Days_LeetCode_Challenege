class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_position=nums[0]
        index=1
        length=len(nums)
        while index<length and maximum_position>=index:
            maximum_position=max(maximum_position,index+nums[index])
            index+=1
        if maximum_position>=length-1:
            return True
        else:
            return False
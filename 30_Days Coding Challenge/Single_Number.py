class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=nums[0]
        length=len(nums)
        for i in range(1,length):
            result=result^i
        return result
        
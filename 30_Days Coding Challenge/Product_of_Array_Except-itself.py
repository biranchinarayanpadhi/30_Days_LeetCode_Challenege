class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1=[]
        nums2=[]
        product=1
        length=len(nums)
        for i in nums:
            product*=i
            nums1.append(product)
        product=1
        for i in nums[::-1]:
            product*=i
            nums2.insert(0,product)
        print(nums1,nums2)
        nums[0]=nums2[1]
        nums[length-1]=nums1[length-2]
        
        i=1
        while i<=length-2:
            nums[i]=nums2[i+1]*nums1[i-1]
            i+=1
        return nums
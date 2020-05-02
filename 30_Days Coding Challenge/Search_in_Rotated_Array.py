class Solution(object):
    def search(self, a, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not a:
            return -1
        
        left,right=0,len(a)-1
        while left<=right:
            mid=(left+right)//2

            if target==a[mid]:
                return mid

            elif a[left]<=a[mid]:
                if a[left]<=target<=a[mid]:
                    right=mid-1
                else:
                    left=mid+1

            else:
                if a[mid]<=target<=a[right]:
                    left=mid+1
                else:
                    right=mid-1
        
        else:
            return -1
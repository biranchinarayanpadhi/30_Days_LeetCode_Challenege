class Solution(object):
    def maxSubArray(self, c):
        current_max=c[0]
        global_max=c[0]
        for i in range(1,len(c)):
            current_max=max(c[i],current_max+c[i])
            global_max=max(global_max,current_max)
        return (global_max)

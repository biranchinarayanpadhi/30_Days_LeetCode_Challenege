class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=j=0
        length=len(prices)-1
        if length<=0:
            return 0
        maxi=0
        sums=0
        while i<length:
            j=i+1
            if prices[j]>prices[i]:
                while j<length+1:
                    diff=prices[j]-prices[i]
                    if maxi<diff:
                        print(diff)
                        maxi=diff
                        j+=1
                        if j==length+1:
                            sums+=maxi
                            return sums
                    else:
                        i=j
                        break
            else:
                i+=1    
            sums+=maxi
            maxi=0
        return sums
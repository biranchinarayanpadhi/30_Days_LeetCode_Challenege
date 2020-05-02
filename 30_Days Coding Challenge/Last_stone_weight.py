class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        length=len(stones)
        if length == 1:
            return stones[0]
        stones=sorted(stones)
        stones=stones[::-1]
        large=stones[0]
        second_largest=stones[1]
        while len(stones) != 1 and len(stones)!=0:
            flag=0
            large=stones[0]
            second_largest=stones[1]
            if large == second_largest:
                stones.pop(0)
                stones.pop(0)
            else:
                stones.pop(0)
                stones.pop(0)
                output=large-second_largest
                i=0
                leng=len(stones)
                if leng==0:
                    return output
                else:
                    while i<leng:
                        if stones[i] < output:
                            stones.insert(i,output)
                            flag=1
                            break
                        elif stones[i] == output:
                            stones.insert(i,output)
                            flag=1
                            break
                        i+=1
                    if flag==0:
                        stones.insert(i,output)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
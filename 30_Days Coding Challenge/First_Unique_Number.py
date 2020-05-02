from collections import OrderedDict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.dicti=OrderedDict()
        
        for elem in nums:
            if elem not in self.dicti:
                self.dicti[elem]=1
            else:
                self.dicti[elem]+=1
        
        

    def showFirstUnique(self) -> int:
        for elem in self.dicti:
            if self.dicti[elem] == 1:
                return elem
        return -1

    def add(self, value: int) -> None:
        
        if value in self.dicti:
            self.dicti[value]+=1
        else:
            self.dicti[value]=1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.temp_dict={}
        self.array=[]
        self.count=0
        
    def get(self, key: int) -> int:
        
        if key in self.map:
            self.array.append(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        temp_dicti={}
        self.count=len(self.map.keys())
        if key in self.map:
            self.map[key]=value
            self.array.append(key)
            
        elif self.count!=self.capacity:
            self.array.append(key)
            self.map[key]=value
            self.count+=1
        else:
            j=len(self.array)-1
            temp_count=0
            while j>=0:
                if self.array[j] in temp_dicti:
                    j-=1
                else:
                    elem=self.array[j]
                    temp_dicti[elem]=0
                    temp_count+=1
                    j-=1
                    if temp_count == self.capacity:
                        del self.map[elem]
                        self.map[key]=value
                        self.array.append(key)
                        del temp_dicti
                        break


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
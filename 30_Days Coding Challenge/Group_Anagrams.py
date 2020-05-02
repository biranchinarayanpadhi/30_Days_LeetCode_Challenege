class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti={}
        temp_array=[]
        final_result=[]
        length=len(strs)
        for i in range(length):
            res="".join(sorted(strs[i]))
            temp_array.append(res)
        
        for i in range(length):
            if temp_array[i] not in dicti:
                dicti[temp_array[i]]=[strs[i]]
            else:
                dicti[temp_array[i]].append(strs[i])
    
        for i in dicti:
            final_result.append(dicti[i])
            
        return final_result
            
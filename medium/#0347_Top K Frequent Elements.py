class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freq = {}
        value = []
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        freq = dict(sorted(freq.items(), key=lambda item: item[1]))
        
        value = list(freq.keys())
        value.reverse()
        
        return value[:k]
      
# [to get frequency] refer: https://www.tutorialspoint.com/list-frequency-of-elements-in-python
# [to sort by value in dict] refer: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# [to get list by key/value] refer: https://www.tutorialspoint.com/How-to-convert-Python-Dictionary-to-a-list

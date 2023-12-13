class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        qua = len(arr)*0.25
        my_dict = {i:arr.count(i) for i in arr}

        key = list(my_dict.keys())
        value = list(my_dict.values())

        idx = value.index(max(value))
        return key[idx]
            

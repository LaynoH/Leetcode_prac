class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        qua = len(arr)*0.25
        my_dict = {i:arr.count(i) for i in arr}

        #for key, value in my_dict.items():
        #    if value>qua:
        #        res = key
        #return res
        res = dict((key,value) for key, value in my_dict.items() if value> qua)
        return list(res.keys())[0]
            
            

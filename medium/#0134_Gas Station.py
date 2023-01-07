class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        if sum(gas)<sum(cost):
            return -1
        
        tank, index = 0, 0
        for i in range(n):
            tank = tank + gas[i] - cost[i]
            if tank < 0: 
                tank, index = 0, i+1
            
        return index

# ref: https://leetcode.com/problems/gas-station/solutions/3011271/python-3-2-6-lines-w-explanation-and-example-t-m-99-98/

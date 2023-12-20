class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        tmp = prices
        tmp.sort()
        if tmp[0]+tmp[1]<=money:
            return money-(tmp[0]+tmp[1])
        return money

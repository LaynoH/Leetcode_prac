class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityA = list(zip(*paths))[0]
        cityB = list(zip(*paths))[1]

        for i in cityB:
            if cityA.count(i)==0 and cityB.count(i)==1:
                return i

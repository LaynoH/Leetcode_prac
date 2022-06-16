class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        
        if (strs[0]==""):
            return ""
        if len(strs)==1:
            return strs[0]
                
        minLen = min(len(i) for i in strs)
        for i in range(minLen):
            prefix.append(strs[0][i])
            for j in range(len(strs)):
                if strs[j][i] and (strs[0][i] != strs[j][i]):
                    if prefix:
                        prefix = prefix[:-1]
                        return ''.join(prefix) 
                    else:    
                        return ""
        return ''.join(prefix)     

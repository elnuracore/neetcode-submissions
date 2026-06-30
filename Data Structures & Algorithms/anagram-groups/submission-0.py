class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashs = {}
        for char in strs:
            key = "".join(sorted(char))
            if key not in hashs:
                hashs[key] = []
            hashs[key].append(char)
        return list(hashs.values())
        
            
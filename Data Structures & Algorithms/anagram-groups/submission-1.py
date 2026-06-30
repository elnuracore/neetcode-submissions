class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_group = {}
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in my_group:
                my_group[word].append(strs[i])
            else:
                my_group[word] = [strs[i]]
        val = list(my_group.values())
        return val
    
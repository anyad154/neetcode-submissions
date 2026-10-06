class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            d[tuple(sorted(strs[i]))]= d.get(tuple(sorted(strs[i])), []) + [strs[i]]
        return list(d.values())
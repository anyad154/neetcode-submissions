class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            d[tuple(sorted(strs[i]))]= d.get(tuple(sorted(strs[i])), []) + [strs[i]]
        good_l = []
        for i in d.values():
            good_l.append(i)
        return good_l
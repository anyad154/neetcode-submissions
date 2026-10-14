from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        new = sorted(list(set(nums)))
        if nums == []:
            return 0
        l = [new[0]]
        for i in range(1, len(new)):
            if new[i] == l[len(l)-1] + 1:
                l.append(new[i])
            else:
                d[tuple(l)] = len(l)
                l = [new[i]]
        d[tuple(l)] = len(l)
        return max(d.values())
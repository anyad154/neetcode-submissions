class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(list(set(nums)))

s = Solution()
s.hasDuplicate([1, 2, 3, 3])
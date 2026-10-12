class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        good_l = [1] * len(nums)
        for i in range (1, len(nums)):
            good_l[i] = good_l[i - 1] * nums[i-1]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            good_l[i] *= postfix
            postfix *= nums[i]
        return good_l
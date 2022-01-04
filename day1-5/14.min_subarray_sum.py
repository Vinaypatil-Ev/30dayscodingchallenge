class Solution:
    def minSubArrayLen(self, target, nums):
        min_len = float("inf")
        left = right = 0
        n = len(nums)
        sums = 0
        while right < n:
            sums += nums[right]
            right += 1
            while sums >= target and left < right:
                min_len = min(min_len, right - left)
                sums -= nums[left]
                left += 1
            
        return 0 if min_len == float("inf") else min_len
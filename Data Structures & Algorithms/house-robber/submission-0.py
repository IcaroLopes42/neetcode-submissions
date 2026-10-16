class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache
        @lru_cache
        def dfs(i, robbed):
            if i>=len(nums):
                return 0
            if robbed:
                return nums[i] + dfs(i+1, False)
            return max(dfs(i+1, True), dfs(i+1, False))
        return max(dfs(0, True), dfs(0, False))
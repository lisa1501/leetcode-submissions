class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            skip = dp[i-1]
            take = nums[i] + (dp[i-2] if i>=2 else 0)
            dp[i] = max(skip, take)

        return dp[-1]


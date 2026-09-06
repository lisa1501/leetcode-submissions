class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        ans = float('-inf')

        window_sum = 0
        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]

            while l <= r and window_sum > target:
                window_sum -= nums[l]
                l += 1

            if window_sum == target:
                ans = max(ans, r - l + 1)

        if ans != float('-inf'):
            return len(nums) - ans
        return -1
        
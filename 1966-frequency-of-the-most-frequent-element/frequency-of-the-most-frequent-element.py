class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sliding window, time: O(nlogn) space: O(n) or O(1) depending on the sorting algorithm
        nums.sort()
        ans = 0
        window_sum = 0

        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]

            while (r - l + 1) * nums[r] - window_sum > k:
                window_sum -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        
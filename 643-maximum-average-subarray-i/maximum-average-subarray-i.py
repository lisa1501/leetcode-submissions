class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float('-inf')
        window_sum = 0
        left = 0
        
        for right in range(len(nums)):
            window_sum += nums[right]

            if right - left + 1 > k:
                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                ans = max(ans, window_sum)

        return ans / k

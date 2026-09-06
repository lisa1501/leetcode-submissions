class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left = 0
            ans = 0
            odd = 0

            for right in range(len(nums)):
                odd += nums[right] % 2

                while odd > k:
                    odd -= nums[left] % 2
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)
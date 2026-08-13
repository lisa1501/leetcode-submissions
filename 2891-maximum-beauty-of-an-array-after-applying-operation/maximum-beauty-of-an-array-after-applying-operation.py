class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # sliding window, time: O(nlogn) space: O(n) or O(1) depending on the sorting algorithm
        nums.sort()
        ans = 0

        l = 0
        for r in range(len(nums)):
            
            while nums[r] - nums[l] > 2 * k:
                l += 1
                
            ans = max(ans, r - l + 1)
        return ans
        
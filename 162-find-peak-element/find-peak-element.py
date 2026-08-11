class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search, time:O(logn), space:O(1)
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
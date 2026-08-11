class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # time:O(ongn), space:O(1)
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # Make mid even
            if mid % 2 == 1:
                mid -= 1
            # the single element is in the right part.
            if nums[mid] == nums[mid+1]:
                lo = mid + 2
            else:
                # Single element is at mid or in the left part.
                hi = mid
        return nums[lo]
        
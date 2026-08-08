class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # time:O(n), space:O(1)
        max_cur = nums[0]
        max_sub = nums[0]

        min_cur = nums[0]
        min_sub = nums[0]

        for i in range(1,len(nums)):
            # max subarray sum ending at i
            max_cur = max(nums[i], max_cur + nums[i])
            # max subarray sum anywhere so far
            max_sub = max(max_sub, max_cur)

            # min subarray sum ending at i
            min_cur = min(nums[i], min_cur + nums[i])
            # min subarray sum anywhere so far
            min_sub = min(min_sub, min_cur)
        return max(max_sub, abs(min_sub))
        
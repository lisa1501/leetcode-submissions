class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        seen = {0:1}
        ans = 0

        for num in nums:
            prefix += num

            if prefix - goal in seen:
                ans += seen[prefix - goal]

            seen[prefix] = seen.get(prefix, 0) + 1
        return ans
        
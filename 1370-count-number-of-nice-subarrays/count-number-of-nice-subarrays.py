class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        seen = {0:1}
        ans = 0

        for num in nums:
            prefix += num % 2

            if prefix - k in seen:
                ans += seen[prefix - k]

            seen[prefix] = seen.get(prefix, 0) + 1
        return ans
        
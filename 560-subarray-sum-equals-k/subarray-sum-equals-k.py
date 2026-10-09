class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sum = 0
        seen = {0 : 1}
        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k
            if needed in seen:
                ans += seen.get(needed, 0)
            
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return ans      
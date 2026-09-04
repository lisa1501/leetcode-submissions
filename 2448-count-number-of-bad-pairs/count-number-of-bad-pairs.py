class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i]
        # i - nums[i] != j - nums[j]
        n = len(nums)
        total = n*(n-1)//2
        seen = {}
        good_pairs = 0
        for i, num in enumerate(nums):
            key = i - num
            good_pairs += seen.get(key, 0) 
            seen[key] = seen.get(key, 0) + 1
        return total - good_pairs
            

        
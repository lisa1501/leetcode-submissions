class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Time:  O(n) Space: O(n)
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        freq = {}
        bad_pairs = 0

        for i, num in enumerate(nums):
            key = i - num
            bad_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        return total_pairs - bad_pairs
        
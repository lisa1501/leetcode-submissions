class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        longest = 0

        for num in seen:
            if num - 1 not in seen:
                longest = 1
                
                while num + 1 in seen:
                    longest += 1
                    num = num + 1

            ans = max(ans, longest)
        return ans

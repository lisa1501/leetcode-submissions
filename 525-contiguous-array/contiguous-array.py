class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        seen = {0:-1}
        length = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -=1
            else:
                prefix += 1

            if prefix in seen:
                length = (i - seen[prefix])
                longest = max(longest, length)
            else:
                seen[prefix] = i
        return longest
        
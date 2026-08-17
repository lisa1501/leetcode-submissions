class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        
        if target == 0:
            return 0

        prefix = 0
        seen = {0:-1}
        ans = len(nums)
        length = 0

        for i in range(len(nums)):
            num = nums[i]
            prefix = (prefix + num) % p
            needed = (prefix - target) % p

            if needed in seen:
                lenght = i - seen[needed]
                ans = min(ans, lenght)

            seen[prefix] = i

        if ans == len(nums):
            return -1
        return ans
        
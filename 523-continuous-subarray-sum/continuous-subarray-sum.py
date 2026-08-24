class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        seen = {0:-1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            reminder = prefix_sum % k

            if reminder in seen:
                if i - seen[reminder] >= 2:
                    return True
            else:
                seen[reminder] = i
        return False

        
        
        
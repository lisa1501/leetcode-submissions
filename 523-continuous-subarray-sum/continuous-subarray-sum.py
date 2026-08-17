class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ans = 0
        prefix = 0
        seen = {0 : -1} 

        for i in range(len(nums)):
            prefix += nums[i]
            reminder = prefix % k

            if reminder in seen:
                if i - seen[reminder] >= 2:
                    return True
            else:
                seen[reminder] = i
        return False
        
        
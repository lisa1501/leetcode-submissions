class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        ans = float('-inf')
        left = 0
        for right in range(len(nums)):
            total += nums[right]

            if right - left + 1 > k:
                total -= nums[left]
                left += 1
            if right - left + 1 == k:
                ans = max(ans, (total / k))

        return ans

            

            

    
        
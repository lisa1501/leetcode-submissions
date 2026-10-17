class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                sub_arr = nums[i:j+1]
                ans += len(set(sub_arr)) ** 2

        ans += n

        return ans 



        
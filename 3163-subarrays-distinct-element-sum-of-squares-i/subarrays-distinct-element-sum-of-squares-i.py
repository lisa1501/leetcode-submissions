class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        # nums = [1,2,1]
                # ^ 
                #   ^
        # 1 len(nums)
        # 2
        # 1
        # 1,2
        # 2,1
        # 1,2,1 len(nums)
        # n = len(nums)
        # n**2 + (1**2) * n = 
        # [1,2,1] 1, 1+1 len(set([1,2,1])) = 2

        # loop thru nums i
        # loop thru j
        # get len of set of (i,j)
        # end we can add set of whole nums len

        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                sub_arr = nums[i:j+1]
                ans += len(set(sub_arr)) ** 2

        ans += n

        return ans 



        
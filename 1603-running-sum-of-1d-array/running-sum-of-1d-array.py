class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums)+1)

        for i in range(len(nums)):
            res[i+1] = res[i] + nums[i]

        return res[1:]
        
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count = 0
        count_target = 0
        for num in nums:
            if num < target:
                count += 1
            if num == target:
                count_target += 1

        res = [-1] * count_target
        for i in range(len(res)):
            res[i] = count

        for i in range(1,len(res)):
            res[i] = res[i-1] + 1
        return res


        
        
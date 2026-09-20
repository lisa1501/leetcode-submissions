class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums_set = set(nums)
        res = []

        for num in range(1, n+1):
            if num not in nums_set:
                res.append(num)
        return res

        
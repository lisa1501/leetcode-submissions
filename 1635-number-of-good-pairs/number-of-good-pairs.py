class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        res = 0

        for num in nums:
            # Every previous occurrence of num
            # creates one new good pair.
            res += freq.get(num, 0)

            freq[num] = freq.get(num, 0) + 1

        return res
        
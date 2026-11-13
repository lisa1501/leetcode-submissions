class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # nums = [1,2,3]
        # min num of nums 1
        # initial moves is 0
        # loop thru nums, cur num, diff of cur num & min num
        # increase moves by diff
        # cur 1, diff =0 moves += diff ,0
        # cur 2, diff =1 moves += diff 1,
        # cur 1, diff =2 moves += diff 2
        # moves =3
        # return moves
        # time: O(n), space: O(1)
        min_num = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_num
        return moves


        
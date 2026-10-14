class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        write = 0
        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        while write < n:
            nums[write] = 0
            write += 1
        return nums
        
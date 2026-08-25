class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
        return write
        
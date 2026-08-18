class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        k = 1

        for read in range(len(nums)):
            if write < k or nums[read] != nums[write-k]:
                nums[write] = nums[read]
                write += 1
        return write
        
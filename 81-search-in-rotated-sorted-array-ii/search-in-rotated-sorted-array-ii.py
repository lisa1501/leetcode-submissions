class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return True

            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid -1
                else:
                    lo = mid + 1
            elif nums[lo] > nums[mid]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            else:
                lo += 1
        return False
        
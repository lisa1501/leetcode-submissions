# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # time:O(logN), space:O(1)
        n = mountainArr.length()
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = (lo + hi) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid 
        peak = lo

        def binary_search(lo, hi, ascending):
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_val = mountainArr.get(mid)

                if  mid_val == target:
                    return mid

                if ascending:
                    if mid_val < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                if not ascending:
                    if mid_val < target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return -1
                
        left_res = binary_search(0, peak, True)
        if left_res != - 1:
            return left_res

        return binary_search(peak+1, n-1, False)      
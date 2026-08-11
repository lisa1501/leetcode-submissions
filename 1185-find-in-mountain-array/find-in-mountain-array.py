# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l = 0 
        r = n -1
        while l < r:
            mid = (l+r) //2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
            else:
                r = mid 
        peak = l

        def binary_search(l, r, ascending):
            while l<=r:
                m = (l+r)//2
                val = mountainArr.get(m)
                if val == target:
                    return m
                if (val < target) == ascending:
                    l = m+1
                else:
                    r = m-1
            return -1

        left_res = binary_search(0, peak, True)
        right_res = binary_search(peak, n-1, False)

        if left_res == -1:
            return right_res
        return left_res
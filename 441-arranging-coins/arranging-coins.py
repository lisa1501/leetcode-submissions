class Solution:
    def arrangeCoins(self, n: int) -> int:
        # binary search , time:O(logn), space: O(1)
        lo = 1
        hi = n
        res = 0
        while lo <= hi:
            mid = (lo + hi) //2
            coins = mid * (mid + 1) //2

            if coins > n :
                hi = mid - 1
            else:
                lo = mid + 1
                res = mid
        return res
            
        
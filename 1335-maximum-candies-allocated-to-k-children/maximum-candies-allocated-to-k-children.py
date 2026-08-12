class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def canFinish(largest):
            children = 0
            for candie in candies:
                children += candie//largest
            return children >= k

        lo = 1
        hi = max(candies)

        while lo < hi:
            mid = (lo + hi + 1) //2 
            # why +1, because we are looking for the very Last True
            # example: lo=4, hi=5. without +1, mid=4,
            # Suppose: canFinish(4) == True => lo =mid=4,hi = 5, Nothing changed!
            # Next iteration:mid = 4, again lo=4, hi=5, get an infinite loop
            # The +1 fixes this,example: lo=4, hi=5. with +1, mid=5, We actually test the upper candidate

            if canFinish(mid):
                lo = mid  
            else:
                hi = mid - 1
        return lo
        
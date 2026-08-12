class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
        # i= 1, s=10, e = 4, 
        # i =4, s=5,  e = 7 
        # ans=(10+5) * min(4,7)=60
        # n> len(speed) => not a case

        # sort of speed, efficiency, but by efficiency, from large to smalll
        # list = [[e, s], [e, s], [e, s],[e, s]]
        # min heap
        # speed sum is 0
        # ans is 0
        # loop through list e, s
        # push s min heap 
        # increase speed sum by s
        # when len(min_heap) > 2:
        # decrease speed sum by pop from min heap
        # ans max of ans, and speed sum after decreasing * current e
        # reutrn ans
        # time: O(nlogn) space:O(n)
        performance = sorted(zip(efficiency, speed), reverse=True)
        print(performance)
        ans = 0
        speed_sum = 0
        min_heap = []

        for e, s in performance:
            heapq.heappush(min_heap, s)
            speed_sum += s

            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            
            ans = max(ans, speed_sum * e)
        
        return ans % (10**9+7)





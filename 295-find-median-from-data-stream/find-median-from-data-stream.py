class MedianFinder:

    def __init__(self):
        # Max heap for the smaller half.
        # Python has a min heap, so store negative values.
        self.max_heap = [] # smaller half, push -num,  [-1]#[-1] # [-2,-1] s
        # Min heap for the larger half.
        self.min_heap = [] # larger half,  push num,  [2] #[2,3] # [3]
        
    def addNum(self, num: int) -> None:
        # add 1, max_heap =[-1]
        # add 2, 2 > -self.max_heap[0]=1, min_heap=[2]
        # find (-(-1) + 2) /2 = 1.5
        # add 3, 2 > -self.max_heap[0]=1,min_heap=[2,3]
        # len(min_heap) > len(max_heap) => max_heap =[-2,-1],min_heap=[3]
        # find len(max_heap) > len(min_heap), float(-heapq.heappop(max_heap))= 2.0
        # Decide which half num belongs to.
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        # Make sure max_heap is not more than
        # one element larger than min_heap. 1  2(<-max)  3(middel) (min->) 4  5
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # Make sure min_heap is never larger than max_heap.
        # badly unbalanced max_heap = 1 2 min_heap = 3 4 5
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # Odd number of elements.
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        # Even number of elements.
        return (-self.max_heap[0] + self.min_heap[0])/2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
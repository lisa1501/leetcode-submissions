class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # 2 friends come to party at the same time not a case
        # in a list (arr, leav, friend) => loop through times, frined idx num, 
        # sort above created list by arr time
        # list of available chairs, loop through created list, chair idx num, min heap, always put or pop smallest available char, sort by chair num
        # list of occupied chairs, [(leaving time, chair num)] min heap, sort by leaving time
        # [(4,0),(3,1),] => at time 4, thru pop we can available chair num (1,0)
        # comparing current arrvie time with first idx of list of occupied[(leaving time, chair num)]
        # if current arrvie time>= first idx of list of occupied,  we can get available chair num , put it into list of available chairs
        # targetFriend == friend, will get chair from list of available , very first index, reutrn first index
        # time: O(nlogn) , space:O(n) n lent(times)

        friends = [(arrive, leaving, i)  for i, (arrive, leaving) in enumerate(times)]
        friends.sort()

        available = [i for i in range(len(times))]
        heapq.heapify(available)
        occupied =[]

        for arrive, leaving, frined in friends:

            while occupied and occupied[0][0] <= arrive:
                chair = occupied[0][1]
                heapq.heappop(occupied)
                heapq.heappush(available, chair)
            chair = heapq.heappop(available)
            if targetFriend == frined:
                return chair

            heapq.heappush(occupied, (leaving, chair))

        




        



        
        
        
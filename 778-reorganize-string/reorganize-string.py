class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s) #{a:3, b:1}
        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap) # [(-3,a),(-1,b)]

        result = []
        prev = None

        while heap or prev:
            if prev and not heap: 
                return ""

            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            cnt += 1 
            #cnt,ch = (-3,a), heap=[(-1,b)],result=[a], cnt=-2<0, prev is none, cnt <0,   heap=[(-1,b)],prev =(-2,a), 
            #cnt,ch = (-1,b), heap=[],     result=[a,b], cnt=0, prev =(-2,a),    heap=[(-2,a)], prev=None,
            #cnt,ch= (-2,a), heap=[], result=[a,b,a], cnt=-1<0, prev =(-1,a),     heap=[], prev =(-1,a),
            #prev =(-1,a),heap=[], return ""
            if prev:
                heapq.heappush(heap, prev) 
                prev = None 

            if cnt < 0:
                prev = (cnt, ch)

        return "".join(result)


        
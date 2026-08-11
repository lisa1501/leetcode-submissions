class TimeMap:
        # time: O(1)-> set(), O(logn) ->get(), space: O(m*n),m:nums of keys, n: the total number of values associated with a key
        
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []

        return self.keyStore[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        
        lo = 0
        hi = len(values) - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            if values[mid][1] > timestamp:
                hi = mid - 1
            else:
                res = values[mid][0]
                lo = mid + 1
            
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
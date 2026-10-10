class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, hour in enumerate(hours):
            sum_val += 1 if hour > 8 else -1
            if sum_val > 0:
                max_len = i + 1
            elif sum_val-1 in mp:
                max_len = max(max_len, i - mp[sum_val-1])
                
            if sum_val not in mp:
                mp[sum_val] = i
        return max_len
        
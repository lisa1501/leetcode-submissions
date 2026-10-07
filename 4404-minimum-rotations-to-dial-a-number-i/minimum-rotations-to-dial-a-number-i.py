class Solution:
    def minRotations(self, s: str) -> int:
        
        n = len(s)
        ans = abs(int(s[0]) - 0)

        if ans > n//2:
            ans = (n - ans)

        for i in range(1,n):
            diff = abs(int(s[i]) - int(s[i-1]))
            if abs(diff) > n//2:
                ans += (n - diff)
            else:
                ans += diff
        
        return ans
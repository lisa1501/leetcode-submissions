class Solution:
    def minRotations(self, s: str) -> int:
        s_list = []
        n = len(s)
        for i in range(n):
            s_list.append(int(s[i]))
        
        ans = abs(s_list[0] - 0)

        if ans > n//2:
            ans = (n - ans)

        print(ans)
        for i in range(1,n):
            if abs(s_list[i] - s_list[i-1]) > n//2:
                ans += (n -  abs(s_list[i] - s_list[i-1]))
            else:
                ans += abs(s_list[i] - s_list[i-1])
        
        return ans
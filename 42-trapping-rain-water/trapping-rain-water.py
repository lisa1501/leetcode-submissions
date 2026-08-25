class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l_max = 0
        r_max = 0

        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                res += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max, height[r])
                res += r_max - height[r]
                r -= 1
        return res
        
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        total = k * threshold
        cur_sum = 0
        l = 0
        for r in range(len(arr)):
            cur_sum += arr[r]

            if r - l + 1 > k:
                cur_sum -= arr[l]
                l += 1

            if r - l + 1 == k and cur_sum >= total:
                ans += 1

        return ans
        
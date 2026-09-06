class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            freq = defaultdict(int)
            l = 0
            ans = 0

            for r in range(len(nums)):
                freq[nums[r]] += 1

                while len(freq) > k:
                    freq[nums[l]] -= 1

                    if freq[nums[l]] == 0:
                        del freq[nums[l]] 
                        
                    l += 1

                ans += r -l + 1

            return ans

        return atMost(k) - atMost(k-1)
        
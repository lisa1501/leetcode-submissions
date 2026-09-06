class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        freq = {}
        ans = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            if r >= 3:
                freq[s[l]] -= 1

                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            if r >= 2 and len(freq) == 3:
                ans += 1

        return ans
        
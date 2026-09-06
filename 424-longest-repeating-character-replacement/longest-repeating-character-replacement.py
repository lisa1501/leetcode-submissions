class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_count = 0
        ans = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1

            max_count = max(max_count, freq[s[r]])

            if r - l + 1 - max_count > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            ans = max(ans, r - l + 1)

        return ans

        
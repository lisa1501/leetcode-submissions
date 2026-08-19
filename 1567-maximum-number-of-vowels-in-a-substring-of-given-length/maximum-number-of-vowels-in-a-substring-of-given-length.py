class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        count = 0 
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = 0

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1

            while r - l + 1 > k:
                if s[l] in vowels:
                    count -=1
                l += 1

            # with length k
            if r - l + 1 == k:
                ans = max(ans, count)
        return ans

        
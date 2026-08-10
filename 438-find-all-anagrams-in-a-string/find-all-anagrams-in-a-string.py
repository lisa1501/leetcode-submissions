class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Time:  O(n + m) n = len(s) m = len(p), Space: O(1), 
        if len(p) > len(s):
            return []

        need = [0] * 26
        window = [0] * 26
        res = []

        for i in range(len(p)):
            need[ord(p[i]) - ord('a')] += 1

        k = len(p)
        for i in range(k):
            window[ord(s[i]) - ord('a')] += 1

        if need == window:
            res.append(0)

        for r in range(k,len(s)):
            window[ord(s[r]) - ord('a')] += 1

            l = r - k
            window[ord(s[l]) - ord('a')] -= 1

            if need == window:
                res.append(l+1)
        
        return res


        
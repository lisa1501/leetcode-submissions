class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = Counter()
        k = len(s1)
        l = 0
        for r in range(len(s2)):
            right_ch = s2[r]
            count_s2[right_ch] += 1

            if r - l + 1 > k:
                left_ch = s2[l]
                count_s2[left_ch] -= 1

                if count_s2[left_ch] == 0:
                    del count_s2[left_ch]

                l += 1

            if count_s2 == count_s1:
                return True
                
        return False
        
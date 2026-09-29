class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and trust ==[]:
            return 1

        trust_me = [0] * (n+1)
        trust_others = [0] * (n+1)

        for a, b in trust:
            trust_me[b] += 1
            trust_others[a] += 1
            

        for i in range(len(trust_me)):
            if trust_me[i] == n-1 and trust_others[i] == 0:
                return i
        return -1


        
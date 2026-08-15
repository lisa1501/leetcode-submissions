class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaker = [0] * (n+1)

        for s, w in edges:
            weaker[w] += 1

        print(weaker)

        champs =[]

        for i in range(n):
            if weaker[i] == 0:
                champs.append(i)

        if len(champs) == 1:
            return champs[0]
        return -1


       
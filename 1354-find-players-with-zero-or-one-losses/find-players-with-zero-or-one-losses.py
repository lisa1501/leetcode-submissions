class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losers = [0] *  100001

        for w, l in matches:
            
            if losers[w] == 0:
                losers[w] = -1

            if losers[l] == -1 or losers[l] == 0:
                losers[l] = 1
            elif losers[l] == 1:
                losers[l] += 1

        lose_zero = [i for i in range(len(losers)) if losers[i] == -1]
        lose_one = [i for i in range(len(losers)) if losers[i] == 1]

        return [lose_zero, lose_one]




            
        

        
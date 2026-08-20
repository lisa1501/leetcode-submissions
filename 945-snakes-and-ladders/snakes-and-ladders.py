class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_position(num):
            quoteint, reminder = divmod(num-1, n)

            row = n - 1 - quoteint

            if quoteint % 2 == 0:
                col = reminder
            else:
                col = n - 1 - reminder

            return row, col


        visited = set()
        visited.add(1)
        q = deque([(1,0)])

        while q:
            state, steps = q.popleft()

            if state == n * n:
                return steps

            for nxt in range(state+1, min(state+6, n*n) +1):
                r, c = get_position(nxt)

                dst = nxt

                if board[r][c] != -1:
                    dst = board[r][c]


                if dst not in visited:
                    visited.add(dst)
                    q.append((dst, steps+1))
        return -1
        
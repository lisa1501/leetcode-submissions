class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ""
        for row in board:
            for num in row:
                start += str(num)

        target = "123450"

        if start == target:
            return 0

        visited = set()
        visited.add(start)
        q = deque([(start, 0)])
        # index num with its neighbor
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        while q:
            for _ in range(len(q)):
                state, steps = q.popleft()
                
                if state == target:
                    return steps

                zero_idx = state.index("0")

                for nei in neighbors[zero_idx]:
                    state_list = list(state)

                    state_list[zero_idx], state_list[nei] = state_list[nei], state_list[zero_idx]

                    new_state = "".join(state_list)

                    if new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, steps+1))

        return -1

            


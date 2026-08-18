class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        if "0000" in deads:
            return -1

        q = deque([("0000", 0)])
        visited = set()
        visited.add("0000")

        while q:
            state, steps = q.popleft()
            if state == target:
                return steps

            for i in range(4):
                cur_num = int(state[i])

                for move in [-1,1]:
                    new_num = (cur_num + move) % 10

                    new_state = state[:i] + str(new_num) + state[i+1:]

                    if new_state not in deads and new_state not in visited:
                        q.append((new_state, steps + 1))
                        visited.add(new_state)
        return -1


        
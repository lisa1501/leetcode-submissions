class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset and beginWord == endWord:
            return 0

        visited = set()
        visited.add(beginWord)
        q = deque([(beginWord, 1)])

        while q:
            for _ in range(len(q)):
                state, steps = q.popleft()
                if state == endWord:
                    return steps

                state_list = list(state)
                for i in range(len(state_list)):
                    original = state_list[i]
                    
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if original != ch:
                            state_list[i] = ch
                            new_state = "".join(state_list)

                            if new_state not in visited and new_state in wordset:
                                visited.add(new_state)
                                q.append((new_state, steps + 1))

                    state_list[i] = original

        return 0
        
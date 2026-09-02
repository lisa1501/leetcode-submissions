class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know_secret = set()
        know_secret.add(0)
        know_secret.add(firstPerson)

        meetings.sort(key=lambda x: x[2])

        i = 0
        while i < len(meetings):
            time = meetings[i][2]

            graph = defaultdict(list)
            people = set()

            while i < len(meetings) and time == meetings[i][2]:
                xi, yi, time = meetings[i]

                graph[xi].append(yi)
                graph[yi].append(xi)

                people.add(xi)
                people.add(yi)

                i += 1

            # multi source bfs, start bfs
            q = deque()
            visited = set()

            for person in people:
                if person in know_secret:
                    q.append(person)
                    visited.add(person)

            while q:
                for _ in range(len(q)):
                    person = q.popleft()

                    for nei in graph[person]:
                        if nei not in visited:
                            visited.add(nei)
                            know_secret.add(nei)
                            q.append(nei)

        return list(know_secret)



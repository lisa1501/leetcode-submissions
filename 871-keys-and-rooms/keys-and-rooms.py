class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            for key in rooms[i]:
                graph[i].append(key)

        used = set()

        def dfs(source):

            used.add(source)

            for nei in graph[source]:
                if nei not in used:
                    dfs(nei)

        dfs(0)
           
        return len(used) == len(rooms)

        
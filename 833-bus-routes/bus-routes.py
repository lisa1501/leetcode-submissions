class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_route = defaultdict(list)

        for route_id, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].append(route_id)

        visited_stops = set()
        visited_stops.add(source)
        visited_routes = set()
        q = deque([(source, 0)])

        while q:
            stop, bus = q.popleft()

            for route_id in stop_to_route[stop]:
                if route_id in visited_routes:
                    continue
                visited_routes.add(route_id)

                for nxt_stop in routes[route_id]:
                    if nxt_stop == target:
                        return bus + 1

                    if nxt_stop not in visited_stops:
                        visited_stops.add(nxt_stop)
                        q.append((nxt_stop, bus+1))
        return -1

        
        
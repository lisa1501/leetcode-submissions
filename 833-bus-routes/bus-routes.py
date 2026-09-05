class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)

        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)

        visited_stops = set()
        visited_stops.add(source)
        visited_buses = set()
        q = deque([(source, 0)])

        while q:
            stop, bus = q.popleft()

            for bus_id in stop_to_buses[stop]:
                if bus_id in visited_buses:
                    continue
                visited_buses.add(bus_id)

                for nxt_stop in routes[bus_id]:
                    if nxt_stop == target:
                        return bus + 1

                    if nxt_stop not in visited_stops:
                        visited_stops.add(nxt_stop)
                        q.append((nxt_stop, bus+1))
        return -1

        
        
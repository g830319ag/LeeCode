class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = min(start, destination)
        e = max(start, destination)
        r_d = 0
        for i in range(s, e):
            r_d += distance[i]
            distance[i]=0
        l_d = sum(distance)
        return min(r_d, l_d)
            

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res_1 = []
        res_2 = []
        for x,y in points:
            d = x**2 + y**2
            res_1.append([d,x,y])
        heapq.heapify(res_1)
        while k > 0:
            d, x, y = heapq.heappop(res_1)
            res_2.append([x,y])
            k -= 1
        return res_2
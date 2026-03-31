class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_1 = abs(heapq.heappop(stones))
            stone_2 = abs(heapq.heappop(stones))

            if stone_1 > stone_2:
                stone_x = stone_1 - stone_2
                stone_x = stone_x * -1
                heapq.heappush(stones,stone_x)
        stones.append(0)
        return abs(stones[0])
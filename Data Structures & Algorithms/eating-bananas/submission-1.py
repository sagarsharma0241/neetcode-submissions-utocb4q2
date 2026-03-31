class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l = 1
        r = max(piles)

        while l <= r :
            hour = 0
            m = (r + l)//2
        
            for p in piles:
                hour += math.ceil(p / m)

            if hour <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        return k        
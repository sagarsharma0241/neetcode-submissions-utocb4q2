class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [(0,1), (0,-1), (1,0),(-1,0)]
        while q and fresh > 0:
            for i in range(len(q)):
                (r_i, c_i) = q.popleft()
                for dr,dc in directions:
                    r = r_i + dr
                    c = c_i + dc
                    if (r < len(grid) and r >= 0 and
                        c >= 0 and c < len(grid[0]) and
                        grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -=1
            time +=1
        return time if fresh == 0 else -1
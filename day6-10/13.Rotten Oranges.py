import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = collections.deque()
        fresh = 0
        rr = [0, 0, 1, -1]
        cc = [1, -1, 0, 0]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1 
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for i in range(4):
                    r = x + rr[i]
                    c = y + cc[i]
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r, c))
        return -1 if fresh != 0 else max(level - 1, 0)
                    
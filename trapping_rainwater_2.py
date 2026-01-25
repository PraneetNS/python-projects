import heapq

grid = eval(input())
m, n = len(grid), len(grid[0])
visited = [[False]*n for _ in range(m)]
heap = []

for i in range(m):
    for j in [0, n-1]:
        heapq.heappush(heap, (grid[i][j], i, j))
        visited[i][j] = True

for j in range(n):
    for i in [0, m-1]:
        heapq.heappush(heap, (grid[i][j], i, j))
        visited[i][j] = True

water = 0
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while heap:
    h, x, y = heapq.heappop(heap)
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            water += max(0, h - grid[nx][ny])
            heapq.heappush(heap, (max(h, grid[nx][ny]), nx, ny))

print(water)

from collections import deque

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for dz, dx, dy in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomatoes[nz][nx][ny] == 0:
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                queue.append((nz, nx, ny))

M, N, H = map(int, input().split())

tomatoes = []
queue = deque()

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        for m, value in enumerate(row):
            if value == 1:
                queue.append((h, n, m))
        layer.append(row)
    tomatoes.append(layer)

bfs()

max_days = 0
for layer in tomatoes:
    for row in layer:
        for value in row:
            if value == 0:
                print(-1)
                exit()
            max_days = max(max_days, value)

print(max_days - 1)  
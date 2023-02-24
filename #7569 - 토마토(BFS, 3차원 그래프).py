import sys
from collections import deque

m, n, h = map(int, input().split())
tomato = [[] for _ in range(h)]

for height in range(h):
    for i in range(n):
        tomato[height].append(list(map(int, sys.stdin.readline().split())))
queue = deque([])

nz = [0, 0, 0, 0, 1, -1]
nx = [0, 0, 1, -1, 0, 0]
ny = [1, -1, 0, 0, 0, 0]

for z in range(h):
    for y in range(n):
        for x in range(m):
            if (tomato[z][y][x] == 1):
                queue.append([z, y, x])


while queue:
    current = queue.popleft()
    x, y, z = current[2], current[1], current[0]

    for i in range(6):
        dx, dy, dz = x+nx[i], y+ny[i], z+nz[i]
        if (0 <= x+nx[i] < m and 0 <= y+ny[i] < n and 0 <= z+nz[i] < h and tomato[dz][dy][dx] == 0):
            queue.append([dz, dy, dx])
            tomato[dz][dy][dx] = tomato[z][y][x] + 1

max_data = 0
flag = True
for z in range(h):
    for y in range(n):
        for x in range(m):
            if (tomato[z][y][x] == 0):
                flag = False
                break
        max_data = max(max_data, max(tomato[z][y]))

if flag:
    print(max_data - 1)
else:
    print(-1)

    
    
'''
이 문제는 이전 토마토 문제와 거의 같은 문제이다. 다만 이전 토마토 문제가 이차원 배열에서의 그래프 탐색이였다면,
이 문제는 삼차원 배열에서의 그래프 탐색 문제이다.

삼차원 배열에서 토마토가 익기위해 탐색해야할 곳이 3차원 모양에서의 십자가 모양으로 총 6곳이다(상,하,좌,우,z축위 상단, z축 아래 하단).
따라서 nz를 추가시켜 총 6곳을 탐색하게 하였다.

이전 토마토 문제를 풀어 별 어려움 없이 코드를 작성할 수 있었다.
'''

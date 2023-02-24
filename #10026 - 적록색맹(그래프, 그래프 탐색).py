import sys
from collections import deque
n = int(input())
sector = []
visited = [[True for _ in range(n)] for _ in range(n)]
for i in range(n):
    sector.append(list(sys.stdin.readline().strip()))

queue = deque([])

normal_count = 0
colorblind_count = 0


nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]

for x in range(n):
    for y in range(n):
        if (visited[y][x] == False):
            continue
        else:
            queue.append([y, x])
            visited[y][x] = False
            while queue:
                current = queue.popleft()
                color = sector[current[0]][current[1]]
                for k in range(4):
                    dx, dy = current[1]+nx[k], current[0]+ny[k]
                    if (0 <= dx < n and 0 <= dy < n and visited[dy][dx] and sector[dy][dx] == color):
                        queue.append([dy, dx])
                        visited[dy][dx] = False
            normal_count += 1

for x in range(n):
    for y in range(n):
        if (visited[y][x] == True):
            continue
        else:
            queue.append([y, x])
            visited[y][x] = True
            while queue:
                current = queue.popleft()
                color = sector[current[0]][current[1]]
                for k in range(4):
                    dx, dy = current[1]+nx[k], current[0]+ny[k]
                    if (0 <= dx < n and 0 <= dy < n and visited[dy][dx] is False):
                        if (color == 'B'):
                            if (sector[dy][dx] == color):
                                queue.append([dy, dx])
                                visited[dy][dx] = True
                        else:
                            if (sector[dy][dx] != 'B'):
                                queue.append([dy, dx])
                                visited[dy][dx] = True
            colorblind_count += 1

print('{} {}'.format(normal_count, colorblind_count))



'''
위 문제는 전형적인 그래프, 그래프 탐색 문제로 같은 구역의 수를 알아내는 문제이다.
하지만 다른 문제와 다른점은, 하나는 R,G,B 3개의 구역의 갯수를 구하는 문제이고,
하나는 (R,G),B 2개의 구역의 갯수를 구하는 문제이다.

구현은 어렵지 않았지만 시간 초과가 발생할까봐 어떻게하면 한번에 이 둘을 셀까 고민하였다.
하지만 도저히 생각이 나지 않았고 각각 따로 구현했는데 시간초과 없이 한번에 맞았다.
'''

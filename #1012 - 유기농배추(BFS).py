n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 칸 기준 상하좌우 살피기


def BFS(x, y):
    queue = [(x, y)]  # 탐색 시작한 좌표 큐에 넣기
    matrix[x][y] = 0  # 방문 했으므로 0으로 처리

    while queue:
        x, y = queue.pop(0)  # deque하고 상하좌우 탐색 시작

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= M or ny >= N or ny < 0):
                continue

            if (matrix[nx][ny] == 1): #상하좌우에서 1이 있을시 이를 queue에 넣고 다시 while문 돌기
                queue.append((nx, ny))
                matrix[nx][ny] = 0 #방문처리하기

#queue에 처음에는 호출한 좌표값 밖에 없었지만 queue.append((nx,ny))로 새로운 좌표 계속 넣어주기
#만약 주변에 1인 좌표가 없다면 queue의 길이가 0이 되므로 자연스럽게 while문을 탈출한다.

for i in range(n):
    M, N, k = map(int, input().split())
    matrix = [[0]*N for _ in range(M)]
    bugs = 0

    for j in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(M):
        for b in range(N):
            if (matrix[a][b] == 1):
                BFS(a, b)
                bugs += 1
                #인접한 1이 있는 좌표를 모두 탐색하므로 한번 호출에 배추벌레 하나가 필요
    print(bugs)

    
'''
BFS를 이용한 문제를 처음 풀어봤다. 학교 전공 수업때 들은 자료구조에서 그래프에 대해 간단히만 배워 
정확한 개념이 정립되지 않은 상태에서 문제를 풀려하니 BFS를 어떻게 구현해야 할지도 모르겠고, 어떤 상황에서 적용시키는지도 잘 몰랐다.
BFS는 queue를 이용해 어느 한 노드에서 인접한 모든 노드를 queue에 차례대로 넣은 다음 만약 방문이 끝나면 방문처리를 하고 dequeue를 해, dequeue한 노드에 대해
똑같이 인접 노드를 방문하고 방문 처리한 다음 queue에 넣는 방식으로 진행된다.

이 문제에서는 방문 처리를 위해 1을 0으로 바꾸는 방식을 택했다.

1012번을 풀면서 아직 그래프에 대한 개념이 정립되지 않았다는 걸 느꼈고, 파이썬 문법에 대한 공부도 틈틈히 해야겠다고 생각했다.
앞으로 문제를 풀면서 개념을 확실히 정립해 가는 것이 좋겠다.
'''

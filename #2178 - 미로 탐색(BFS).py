import sys

n, m = map(int, input().split())
graph = []
distance = [[1 for _ in range(m+1)] for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

queue = [[0, 0]] 
queue_pass = [] #방문표시

while queue:
    current = queue.pop(0)
    queue_pass.append(current) #방문표시
    x = current[0] #queue에서 꺼낸 것의 x좌표
    y = current[1] #queue에서 꺼낸 것의 y좌표
    
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]

    for i in range(4):
        if (0 <= x+nx[i] < m and 0 <= y+ny[i] < n): #범위 지정
            if ([x+nx[i], y+ny[i]] not in queue and [x+nx[i], y+ny[i]] not in queue_pass): #방문하지 않은 노드
                if (graph[y + ny[i]][x+nx[i]] == 1): #지나갈 수 있는 길
                  
                    distance[y+ny[i]][x+nx[i]] = distance[y][x] + 1 #현재의 거리 = 이전 거리 + 1
                    queue.append([x+nx[i], y+ny[i]])

print(distance[n-1][m-1])


'''
이 문제는 좌표축(그래프)가 주어졌을때, 시작점(0,0) 에서 끝점(m,n)까지 최단 거리를 구하는 문제이다.
최단거리라는 단어를 보자마자 BFS로 풀어야겠다고 생각이 들었다.

상하좌우로만 움직일 수 있기 때문에, nx, ny를 통해 상하좌우를 구현하였다.

이전에 풀었던 문제들과 비슷한 문제였기 때문에 막힘 없이 한번에 풀기 쉬웠다.
어느정도 BFS 문제를 풀다보니 익숙해진 것 같다.
'''

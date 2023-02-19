import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1].append(y)
    graph[y-1].append(x)
    #인덱스와 값으로 그래프 구현하기


visited = [] #방문 처리 용도 리스트
connected = 0 #연결된 요소의 개수

#BFS 구현하기
def bfs(current):
    global visited
    queue = deque([current]) #시간복잡도 상 deque로 사용
    
    while (queue):
        current = deque.popleft(queue)
        visited.append(current)
        for i in range(len(graph[current-1])):
            if (graph[current-1][i] not in queue and graph[current-1][i] not in visited):
                queue.append(graph[current-1][i])


for i in range(len(graph)):
    if (len(graph[i]) == 0):
        visited.append(i+1)
        connected += 1
        #만약 해당 노드와 연결된 노드가 하나도 없을 시, 요소 한개로 판단하고 + 1
    for j in range(len(graph[i])):
        if (graph[i][j] not in visited):
            current = graph[i][j]
            bfs(current)
            connected += 1
            #방문하지 않은 노드에 대해(새로운 요소라 판단) bfs 함수 다시 실행

print(connected)



'''
해당 문제는 전형적인 그래프, BFS, DFS 문제로 연결된 요소의 개수를 알아내는 문제이다.
이러한 유형의 문제를 많이 풀어봐서 구현은 어렵지가 않았지만, 시간복잡도를 해결하는데 시간을 조금 썼다.

처음에는 while문을 이용해 구현했지만, 자꾸만 시간 초과가 발생하였고, 아무것도 연결되지 않은 간선에 대해서는 해결하지 못하였다.

따라서 for문을 이용해 그래프를 탐색하는 방법으로 전환하였다.


처음 bfs문제를 풀때보다 코드가 많이 깔끔해지고 간결해진 것 같다.
아마도 deque를 사용하고, 함수를 사용해 가독성과 간결함이 배가 된 것 같다.
앞으로 더 많이 문제를 풀어 코드를 깔끔하게 다듬는 노력을 해야겠다.
'''

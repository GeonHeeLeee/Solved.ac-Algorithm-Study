import sys
n, m, v = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if (b in graph[a-1]):
        continue
    else:
        graph[a-1].append(b)
    if (a in graph[b-1]):
        continue
    else:
        graph[b-1].append(a)

# graph[k]이면 k+1과 연결된 모든 노드 저장

stack = []  # DFS Stack
queue = []  # BFS Queue
queue_pass = []  # BFS 방문표시
stack_pass = []  # DFS 방문표시


if (n <= m):
    flag = n
else:
    flag = m + 1
#반복문 탈출조건 예외처리
#경우 1 : 노드의 수 <= 간선의 수
#경우 2 : 노드의 수 > 간선의 수


# DFS

crnt = v  # 시작점
stack.append(v)
stack_pass.append(v)

if (len(graph[crnt-1]) != 0):  # 아무것도 연결되지 않았을 때 예외처리
  
    while (len(stack_pass) < flag):
        count = 0  # 연결된 모든 노드 방문 카운트
        graph[crnt-1].sort()  # 작은 순서대로 방문이므로 정렬
        
        for i in range(len(graph[crnt-1])):
            if (graph[crnt-1][i] in stack_pass):
                count += 1  # 방문한 것 카운트
                
            else:
                stack.append(graph[crnt-1][i])  # stack에 추가
                stack_pass.append(graph[crnt-1][i])  # 방문표시
                crnt = graph[crnt-1][i]
                break
                
            if (count == len(graph[crnt-1])):  # 연결된 모든 노드를 방문했을때
                stack.pop()  # 스택에서 꺼내고
                crnt = stack[-1]  # 스택의 맨위의 노드에서 방문하지 않은 연결노드 다시 탐색
                break


# BFS

#시작점
queue.append(v)
queue_pass.append(v)
queue.pop(0)

#작은 순서대로 방문이므로 정렬해야하지만 DFS에서 정렬했으므로 시간 복잡도상 정렬 X

if (len(graph[v-1]) != 0):  # 아무것도 연결되지 않았을 때 예외처리
  
    for i in range(len(graph[v-1])):
        queue.append(graph[v-1][i])  # BFS이므로 인접한 모든 노드 Queue에 넣기
        
    while len(queue_pass) < flag:
        crnt = queue.pop(0)
        queue_pass.append(crnt)
        #queue에서 dequeue 후, dequeue한 노드에 대해 인접 노드 넣기
        
        for i in range(len(graph[crnt-1])):
            if (graph[crnt-1][i] in queue_pass or graph[crnt-1][i] in queue):
                continue
                #DFS와 다르게 방문처리한 Queue_pass와 방문했지만 방문처리 하지 않은 Queue에 있는 것 모두 확인
                
            queue.append(graph[crnt-1][i])
            #방문하지 않은 것 Enqueue
            

# 출력
for i in stack_pass:
    print(i, end=' ')
print()
for i in queue_pass:
    print(i, end=' ')
    
    
    
'''
이 문제는 정통 BFS, DFS 문제이다. 
처음에 그래프를 어떻게 구현할지 고민하는 도중, 이차원 배열로 다음과 같은 방식으로 구현하면 좋겠다고 생각되어 이차원 배열로 구현하였다.

방식은 다음과 같다.

graph[현재노드-1][현재 노드와 연결된 노드의 집합]



BFS는 금방 구현했지만, DFS에서 시간을 많이 잡아 먹혔다.
노드 포인팅을 잘못해 계속해서 에러가 발생해, 이를 해결하는데 오래걸렸다.

처음 그래프를 구현하는 것부터 방문처리, BFS, DFS를 구현하는 것은 거의 처음이라 이 방식으로 하는 것이 맞나 의심이 계속 들었지만
다른 사람의 코드를 참고하지 않고 나만의 방식으로 구현하여서 매우 뿌듯하다.

이 문제로 인해 BFS, DFS에 대한 개념이 어느정도 잡힌 것 같다.
추후 다른 사람의 코드를 참고하여 다른 구현 방식도 알아보면 좋을 것 같다.
'''

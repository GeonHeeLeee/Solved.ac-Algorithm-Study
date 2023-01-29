import sys
n,m = map(int, input().split())

friendList = [[] for i in range(n)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    if(b not in friendList[a-1]):
        friendList[a-1].append(b)
    if(a not in friendList[b-1]):
        friendList[b-1].append(a)
    else:
        continue
fl_result = []
for j in range(n):
    queue = []
    queue_pass = []
    crnt = j+1
    result = {crnt : 0}
    queue.append(crnt)
    for i in range(n):
        crnt = queue.pop(0)
        queue_pass.append(crnt)
        for k in range(len(friendList[crnt-1])):
            if(friendList[crnt-1][k] not in queue_pass and friendList[crnt-1][k] not in queue):
                queue.append(friendList[crnt-1][k])
                result[friendList[crnt-1][k]] = result[crnt] + 1
            else:
                continue
    fl_result.append(sum(result.values()))
        

print(fl_result.index(min(fl_result))+1)

'''
사람의 번호와 관계를 주고 다리 건너 아는 사람의 최소값을 찾는 문제이다.
어떤 방식으로 풀어야 될지 생각 중, BFS가 가장 적합하다고 판단되어 BFS로 구현하였다.

다리 건너 아는 사람의 최소값은 결국 그래프 문제로, 현재 번호에서 다른 번호로 가는 최소의 거리를 찾는 문제로
해석할 수 있었다.

최소값은 현재 번호에서 다른 사람의 번호로 가는 길에 +1를 해주는 방식으로 구현하였다.

BFS 문제를 계속 풀다보니 어떤 문제를 BFS로 구현하는지, 구현 하는 방식도 익숙해진 것 같다.
이제 DFS와 Dynamic Programming을 숙달 시켜야 될 것 같다.
'''

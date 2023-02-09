import sys
n=int(input())
computer = [[] for _ in range(n)]
m = int(input())
for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    if(num1 not in computer[num2-1]):
        computer[num2-1].append(num1)
    if(num2 not in computer[num1-1]):
        computer[num1-1].append(num2)
count = 0
queue = [1]
queue_pass = []
current = 1
while(queue):
    current = queue.pop(0)
    queue_pass.append(current)
    count += 1
    for i in range(len(computer[current-1])):
        if(computer[current-1][i] not in queue and computer[current-1][i] not in queue_pass):
            queue.append(computer[current-1][i])
    
print(count-1)

'''
이 문제는 전형적인 그래프 문제이다. 1번 노드와 연결된 노드의 수를 구하는 것과 같다고 생각할 수 있다.
나는 BFS방식으로 풀었지만 DFS으로도 풀 수 있을 것 같다.

처음 이중리스트에 해당 노드와 연결된 모든 노드를 중첩되지 않게 추가한다.
*만약 n번 노드와 3,4,5가 연결되어 있으면 computer[n-1] = [3,4,5]

그 다음 queue를 이용해 구현한다.

BFS가 익숙해졌다보니, 문제 구상, 구현하는데 3~5분 정도밖에 걸리지 않았다.
'''

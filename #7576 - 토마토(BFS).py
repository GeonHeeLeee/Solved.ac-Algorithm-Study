import sys
from collections import deque

m, n = map(int, input().split())
tomato = []
queue = deque([])

for i in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

for y in range(n):
    for x in range(m):
        if (tomato[y][x] == 1):
            queue.append([y, x]) #출발점 queue에 넣기

nx = [0, 0, -1, 1]
ny = [1, -1, 0, 0] #상하좌우 판단을 위한 배열 선언


while (queue):
    current = queue.popleft() 
    y = current[0]
    x = current[1]
    for j in range(4):
        if (0 <= x+nx[j] < m and 0 <= y+ny[j] < n):
            if (tomato[y+ny[j]][x+nx[j]] == 0): #0이고 범위 내에 있으면 queue에 넣기
                queue.append([y+ny[j], x+nx[j]])
                tomato[y+ny[j]][x+nx[j]] = tomato[y][x] + 1 #현재거리 = 이전거리 + 1


max_distance = 0
flag = True
for y in range(n):
    for x in range(m):
        if(tomato[y][x] == 0):
            flag = False 
            break
            #만약 0이 있을 시, 안 익은 토마토가 존재한다는 뜻이므로 break하고 바로 -1 출력
            
    max_distance = max(max_distance,max(tomato[y])) #최대값 = 최단거리 찾기
    
if (flag):
    print(max_distance-1) #처음 시작이 1로 시작했으므로 -1 해주기
else:
    print(-1)

'''
이 문제는 전형적인 BFS 문제로, 최단거리를 구하는 것으로 해석 할 수 있다.
출발점(토마토가 처음 익기 시작한 곳)이 여러개 일 경우 어차피 처음 시작이 1이므로 이전 것에다 +1을 해주면 되므로 따로 로직을 생각할 필요가 없었다.

처음 출발지를 모두 queue에다 넣어주고 이에 대해 BFS를 이용하여 최단거리를 구하면 되었다.
BFS를 구현하는것은 쉬웠지만 자꾸 시간초과가 발생해 애를 먹었다.

도저히 코드를 간결화하는것은 어렵다고 생각되어 구글링을 했더니, deque 모듈을 쓰지 않아서 시간복잡도가 초과된다고 나와 있었다.
조금 더 검색을 해보니, 리스트의 pop(0)은 뒤에 있는 모든 원소를 앞으로 당겨와야 하기 때문에 시간복잡도가 O(n)이 되고, deque의 popleft()는 O(1)이라 시간복잡도 차이가 많이 난다고 했다.

그래서 deque만 import 해서 코드 수정을 하니 통과하였다.



deque는 리스트와 사용법이 거의 동일하다.
from collections import deque 로 import 하고,

queue = deque([])로 빈 배열을 선언한다.
만약 queue = deque('love')로 할 시, queue == ['l','o','v','e'] 와 같이 분리 되어 초기화 된다.

pop(0) == popleft
append = append

이외에도
appendleft, insert, remove, reverse 등 다양한 함수를 지원한다.

이제부터 시간복잡도를 위해 그래프 문제는 deque를 이용하여 풀어야겠다.
'''

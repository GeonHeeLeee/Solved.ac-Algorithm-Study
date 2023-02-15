def bfs(n):
    queue = []
    queue.append(n)
    while queue:
        current = queue.pop(0)
        if(current == k):
            print(distance[current])
            break
        for x in (current + 1, current - 1, current * 2):
            if(0 <= x <= MAX and distance[x] == 0):
                distance[x] = distance[current] + 1
                queue.append(x)

n,k = map(int, input().split())
MAX = 10**5
distance = [0]*(MAX+1)
bfs(n)



'''
이 문제는 BFS로 최단경로를 찾는 문제이다.
처음에는 DP로 푸는 것인줄 알았으나, 연결된 모양이 그래프이고 두 노드 간 최단 경로를 찾는 문제이기 때문에 BFS로 풀어야 한다.
BFS의 방문 경로나 그래프를 구현하는 것은 몇번 해봐서 익숙했으나, 최단 거리를 구하는 것은 처음이여서 구현이 어려웠다.


반복문을 통해 변수에 +1을 해주는 것이 아닌, distance라는 모든 초기값이 0인 배열을 선언해 각 레벨마다 이전값 +1을 해주는
방식을 사용하여 문제를 풀었다.

이 방식을 사용하니 코드도 간결해지고 직관적이여서 이해하기도 쉬웠다.

아직 그래프 탐색이 익숙하지 않으니 문제를 더욱 많이 풀어봐야겠다.
'''

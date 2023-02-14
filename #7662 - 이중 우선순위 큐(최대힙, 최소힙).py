import sys
import heapq

t = int(input())

for i in range(t):
    k = int(input())
    visited = [1 for _ in range(k)] #삭제 했는지 알기 위해
    count = 0 #heap이 빈 상태에서 pop하는것을 막기 위해 선언
    max_heap = []
    min_heap = []
    for j in range(k):
        command, num = sys.stdin.readline().split()
        if(command == 'I'):
            count += 1
            heapq.heappush(max_heap, (-int(num),int(num), j)) 
            heapq.heappush(min_heap, (int(num),j))
            #숫자마다 고유 번호 부여, 같은 숫자가 입력되도 고유 번호가 달라서 다르게 인식됨

        else:
            if(count <= 0):
                #만약 힙의 크기가 0일시 pass : push보다 pop의 수가 많을 시
                pass
            else:
                count -= 1 
                if(num == '-1'):
                    while(True): #max_heap에서 삭제 되었을 수도 있기 때문에 구현
                        pop_num = heapq.heappop(min_heap)
                        if(visited[pop_num[1]] == 1): #만약 max_heap에서 삭제되지 않았으면
                            visited[pop_num[1]] = 0 #삭제 표시 후 break
                            break
                else:
                    while(True): #min_heap에서 삭제 되었을 수도 있기 때문에 구현
                        pop_num = heapq.heappop(max_heap)
                        if(visited[pop_num[2]] == 1): #만약 min_heap에서 삭제되지 않았으면
                            visited[pop_num[2]] = 0 #삭제 표시 후 break
                            break
    min = 0 
    max = 0
    if(count <= 0): #push보다 pop의 횟수가 많은 경우 : heap이 빈 상태임
        print('EMPTY')
    else: 
        for i in range(len(min_heap)): #min_heap에서 삭제 표시 한 것 제외 최솟값 출력
            num = heapq.heappop(min_heap)
            if(visited[num[1]] == 1):
                min = num[0]
                break
        for i in range(len(max_heap)): #max_heap에서 삭제 표시 한 것 제외 최댓값 출력
            num = heapq.heappop(max_heap)
            if(visited[num[2]] == 1):
                max = num[1]
                break
        print('{} {}'.format(max,min))
        
        
'''
보통 힙은 최대힙, 최소힙 따로 구현하는데, 이 문제는 특이하게 최대힙, 최소힙을 같이 구현해야 한다.
파이썬에서 지원하는 heapq는 최소힙에서 최대값을 못 지우고, 최대힙에서 최솟값을 못 지우기 때문에 두개의 힙을 선언해야 한다.
*엄밀히 따지면 지울 수 있긴한데 시간복잡도상 문제에선 불가능

이전 문제에서 풀었듯이, 최대힙은 힙이 튜플의 첫번째 원소를 기준으로 판단하여 heap을 구성하기 때문에
(-num, num)와 같은 방식으로 push를 하면 최대힙이 구성된다.

하지만 두개의 힙을 구성하면 최소힙에서 최솟값을 pop할시, 최대힙에서도 해당 값을 지워야 한다는 문제가 있었다.

따라서 실질적으로 삭제하는 대신, 삭제 표시(visited)을 선언하여 따로 삭제 표시를 해 두었다.
for문을 돌면서, 각각의 숫자의 고유번호를 표시해 heap에 추가할 때 튜플 형식으로 같이 heap에 추가하였다.
따라서 삭제 표시를 할때 각각의 고유번호에 해당하는 인덱스의 값을 바꾸어주면 삭제표시가 되게 하였다.

또한 최소힙에서 최솟값을 삭제하려고 할때, 이미 최대힙에서 삭제가 되었을수도 있기 때문에, while문을 통해 삭제가 되지 않을 최솟값이
나올때까지 반복문을 돌게 하였다.

또한 push보다 pop의 경우가 많을 경우 명령을 무시해야하기 때문에 count 변수를 선언하여 이를 해결하고,
힙이 비었다는 것 또한 알 수 있게하였다.




heapq를 사용한지 오래되어 기억이 가물가물 했는데, 이 문제를 통해 복습하게 되어 개념을 확실히 다질 수 있었고,
heap에 대해서도 복습을 하게 되어 의미가 큰 문제였던 것 같다.

그리고 또한 삭제 표시를 하는 방법도 터득한 것 같다.
'''
 
 

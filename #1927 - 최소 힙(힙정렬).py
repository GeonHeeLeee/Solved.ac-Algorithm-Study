import sys
n = int(input())
heap = []
min = 2**31
for i in range(n):
    num = int(sys.stdin.readline().strip())
    if(num == 0):
        if(len(heap) == 0):
            print(0)
        else:
            for i in heap:
                if(i < min):
                    min = i
            print(min)
            heap.remove(min)
            min = 2**31
    else:
        heap.append(num)
        
        
'''
위에 코드가 처음에 내가 구현한 코드이다. 이론상으론 문제가 없었지만, 시간초과가 자꾸 발생하였다.
그래서 자료 구조때 배운 힙(heap)을 생각하였다.

힙은 max-oriented heap, min_oriented heap이 있다.
이진트리방식으로, min-oriented heap에서는 기준 값보다 작으면 왼쪽, 크면 오른쪽에 배치한다.

그리고 값을 삽입하거나 삭제할시에는 up-heap-bubbling, down-heap-bubbling을 사용하여 정렬한다.
삭제는 항상 루트 값을 삭제하며, 맨 끝의 값을 루트로 올려 down-heap-bubbling으로 다시 정렬한다.

파이썬에서는 heap 모듈을 지원한다.
오늘은 파이썬 heap 모듈 사용 방법을 배웠다.

import heapq로 import한다.
heapq에는 3가지 함수가 있다.

1. heappush(heap,num) - heap에 값 넣기
2. heappop(heap) - 최상단 값 빼기
3. heapify(list) - 리스트를 힙으로 만들기

*파이썬에서의 힙은 min-oriented로 되어 있기 때문에, max-oriented로 만들려면 다음과 같은 방식을 거치면 된다.

for i in range(n):
  heapq.heappush(heap, (-num, num))
 
이 방식을 사용할 시, 튜플의 첫번째 원소로 min-oriented을 만들어서 max-oriented가 된다.


아래의 코드는 heapq 모듈을 사용하여 다시 짠 코드이다.
'''


import sys
import heapq
n = int(input())
heap = []
result = []
for i in range(n):
    num = int(sys.stdin.readline())
    if(num == 0):
        if(len(heap) == 0):
            result.append(0)
        else:
            result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)

for i in result:
    print(i)

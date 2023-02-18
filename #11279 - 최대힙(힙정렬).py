import heapq

n = int(input())
max_heap = []

for i in range(n):
    num = int(input())
    if(num == 0):
        if(len(max_heap) == 0):
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap,(-num, num))


'''
위 문제는 최대힙을 구현하여, push, pop을 구현하는 문제이다.
힙을 구현하는것은 익숙하여 바로 문제를 풀고 맞췄다.

heapq 라이브러리를 복습하는데 도움이 되었다.

max_heap을 만들기 위해서는, 튜플 형태로 (-num, num)위와 같이 push를 해야한다.
왜냐하면 heapq는 튜플의 첫번째 원소를 기준으로 정렬을 하기 때문에 위와 같은 방식으로 push시, 최댓값이 된다.

이후 heapq.heappop(), heapq.heappush()를 이용하여 구현하면 된다.
'''

import sys

n,m = map(int, sys.stdin.readline().split())
treeList = list(map(int, sys.stdin.readline().split()))

min_height = 0
max_height = max(treeList)

while(min_height <= max_height):
    sum = 0
    height = (min_height + max_height) // 2
    for i in treeList:
        if(i > height):
            sum = sum + (i - height)
        
    if(sum >= m):
        min_height = height + 1
    else:
        max_height = height - 1

print(max_height)

'''
최솟값과 최대값이 주어지고 이 사이에서 알맞은 값을 찾고 싶을 시 이진탐색을 사용하면 된다.

고려하지 못 했었던 것
탈출 조건 - 최소가 최대를 역전하는 상황이 나오는데, 이를 탈출 조건으로 보고 이 값이 찾는 값이 된다.
'''

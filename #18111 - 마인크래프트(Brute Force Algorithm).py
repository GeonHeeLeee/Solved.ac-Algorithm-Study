import sys
n,m,b = map(int, sys.stdin.readline().split())
block = []
block = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_time = sys.maxsize
min_floor = 0
for floor in range(257):
    take_block = 0
    use_block = 0
    for i in range(n):
        for j in range(m):
            if(block[i][j] >= floor):
                take_block += block[i][j] - floor
            else:
                use_block += floor - block[i][j]

    if(take_block + b >= use_block):
        if(take_block * 2 + use_block <= min_time):
            min_time = take_block * 2 + use_block
            min_floor = floor
print(min_time, min_floor)

'''
이도 마찬가지로 BruteForce 알고리즘을 이용해 모든 층수에 대한 경우를 비교한다.
시간복잡도를 고려하기 전에 가장 기본적인 BruteForce 알고리즘을 떠올려 구현부터 해보자.
만약 구현에 성공했지만 시간 초과가 뜬다면 이는 다른 알고리즘을 생각하면 되니 구현을 우선적으로 하자.
'''

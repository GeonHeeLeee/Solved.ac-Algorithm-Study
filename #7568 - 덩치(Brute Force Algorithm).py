import sys

n = int(input())
data = []
result =[0]*n

for i in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    data.append((weight,height))


for i in range(n):
    count = 1
    for j in range(n):
        if(j == i):
            continue
        if(data[i][0] < data[j][0] and data[i][1] < data[j][1]):
            count += 1
    result[i] = count

for i in range(n):
    print(result[i])
    
    
'''
대부분 문제를 풀 때, 시간복잡도를 최소화하려고 노력하다보니, 가장 기본적인 브루트포스 알고리즘을 생각하지 못했다.
반복문을 돌면서, 자신의 몸무게와 키보다 큰 사람이 있으면 count를 +1 해주는 방식으로 구현하였다.
이는 시간복잡도가 O(n^2)이 들지만 테스트케이스의 갯수가 적어 시간 초과가 발생하지 않는다.

중요한 것은 반복문 속 두번째 반복문에서 범위가 (i, n)이 아닌 그냥 (n)이라는 것이다.
'''
    

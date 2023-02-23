'''
이 문제는 n이 주어지고 m 길이의 문자열 s가 주어질때, s에서 "IO"*n + 'I'의 개수를 찾는 문제이다
*만약 n == 2일시, IOIOI

시간복잡도에 따라 50점, 100점으로 나뉘었었는데 처음에는 계속 50점만 맞아서 어떻게하면 시간복잡도를 줄일지가 관건이였다.
아래는 50점을 맞은 코드이다.

거의 브루트포스 알고리즘 방식으로 하나씩 다 비교해가면서 풀었었다.
'''


import sys
n = int(input())
m = int(input())
s = sys.stdin.readline().strip()

count = 0
current = 0

while current+n*2 < m:
    if(s[current:current+n*2+1] == n*'IO'+'I'):
        count += 1
    current += 1
print(count)

'''
하지만 시간복잡도를 줄이기 위해 아래의 코드를 생각해냈다.
'''


import sys
n = int(input())
m = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

count = 0
answer = 0
current = 0

while current+2 < m:
    if(s[current:current+3] == 'IOI'):
        count += 1
        current += 2
        if(count == n):
            count -= 1
            answer += 1
    
    else:
        current += 1
        count = 0

print(answer)

'''
이는 IOIOIOIOI들이 반복되는 수열이기 때문에 가능한 코드인데, 만약 s = IOIOI에서 IOI를 찾을려면 (IOI, OI) (IO, IOI) 위와 같이 겹치는 2개가 있다.
따라서 IOI의 개수를 센 다음, IOI의 개수를 하나 빼 준다음, 다시 IOI가 나오면 정답 개수를 하나씩 올린다.
이 코드는 맨 처음 작성한 코드보다 순회하는 시간이 빨라져 훨씬 시간복잡도 상으로 이득이다.
'''

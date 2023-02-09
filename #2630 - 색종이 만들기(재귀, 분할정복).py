import sys

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
num_1 = 0
num_0 = 0


def paper_check(x, y, n):
    global num_0, num_1
    current = paper[y][x]
    for ny in range(y, y+n):
        for nx in range(x, x+n):
            if (paper[ny][nx] != current):
                for i in range(2):
                    for j in range(2):
                        paper_check(x+n//2*i, y+n//2*j, n//2)
                return
    if (current == 1):
        num_1 += 1
    elif (current == 0):
        num_0 += 1


paper_check(0, 0, n)

print(num_0)
print(num_1)


'''
이전에 풀었던 문제와 비슷한 유형의 분할정복, 재귀 문제이다.
만약 하나라도 다른 것이 있을 시, 구역을 4개로 나눈 다음, 4개 모두 따로 함수를 호출한다.
다르지 않으면 재귀함수를 호출하지 않으므로, 각 숫자의 맞는 값을 +1 한다.

사각형이 1개로 최소로 쪼개졌을때에는 current == paper[ny][nx]가 무조건 성립하므로, 탈출 조건을 따로 만들지 않아도 된다.
재귀함수를 호출 시, 이전 함수는 필요 없기 때문에 return 시켜준다.
'''


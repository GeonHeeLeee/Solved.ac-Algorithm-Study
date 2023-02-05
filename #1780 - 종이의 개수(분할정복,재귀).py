import sys
n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
    #2차원 리스트로 좌표 생성
   
count_0 = 0
count_1 = 0
count_sub1 = 0


def paper_check(n, x, y):
    global count_1, count_0, count_sub1
    
    current = paper[y][x]
    
    for ny in range(y, y+n):
        for nx in range(x, x+n):
          #하나씩 증가하면서 다른 것 찾기
          #현재 구역에서 가장 왼쪽 상단에 있는 좌표(x,y)에서 n만큼 더한 구역 탐색
          
            if (paper[ny][nx] != current):
              #만약 하나라도 다를 시, 9개의 구역으로 쪼개서 재귀 방식으로 다시 호출
              
                for i in range(3):
                    for j in range(3):
                        paper_check(n//3, x + j*n//3, y + i*n//3)
                        #만약 원래 n == 9였다면 쪼갤 시, n == 3인 구역이 9개가 생기므로 이를 재귀함수로 호출
                return
                #1*1 행렬은 if(paper[ny][nx] != current) 가 성립 할 수 없으므로 자동적으로 탈출조건 성립
                
    if (current == 0):
        count_0 += 1
    elif (current == 1):
        count_1 += 1
    else:
        count_sub1 += 1


paper_check(n, 0, 0)
print(count_sub1)
print(count_0)
print(count_1)


'''
처음에는 BFS로 풀려고 시도했었다. 하지만 이 문제는 분할 정복으로 푸는 문제였다.
원리와 방식은 알았지만 구현과 재귀함수 좌표 설정에서 난항을 겪었다.
재귀 함수로 호출 시 머리 속이 매우 복잡해져서 많이 헷갈렸었다.

사실 구역을 탐색하다 다른 것 하나라도 나오면 바로 쪼개고 재귀 호출을 하면 되는 문제라 간단했지만 익숙하지 않아서 해맸던 것 같다.
분할 정복과 재귀 문제를 더욱 많이 풀어봐야겠다.
'''
            

n = int(input())
import sys
quad = []
for i in range(n):
    quad.append(list(sys.stdin.readline().strip()))
    
result = ''

def quad_tree(n,x,y):
    global result
    
    current = quad[y][x]
    
    for ny in range(y,y+n):
        for nx in range(x,x+n):
            
            if(quad[ny][nx] != current): #만약 하나라도 다를 시 바로 재귀함수 호출
                result += '(' #새로운 호출 시, 괄호를 열음
                for i in range(2):
                    for j in range(2):
                        quad_tree(n//2,x+j*n//2,y+i*n//2) #4구역으로 나누어 함수 다시 호출
                        
                result += ')' #호출이 끝날 시, 괄호 닫기
                return
    result += current #결과 
    
quad_tree(n,0,0)
print(result)

'''
이 문제는 분할정복, 재귀를 사용하는 방식으로 #1780 문제와 거의 흡사하다.
하나라도 다른것이 있을 시, 바로 재귀 방식을 이용해 함수를 다시 호출한다.
1X1 행렬이 되면 무조건 조건을 만족 할 수 밖에 없는데, 이때 결과를 출력한다.

딱 보고 분할정복, 재귀를 사용해야겠다고 생각하고 이전의 풀었던 #1780을 떠올려 쉽게 해결할 수 있었다.
'''

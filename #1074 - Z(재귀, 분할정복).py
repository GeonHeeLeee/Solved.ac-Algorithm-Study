n,r,c = map(int, input().split())
matrix = [[0]*2**(n) for _ in range(2**(n))]
count = 0
def Z(x,y,n):
    global count
    if(n == 1):
        for i in range(2):
            for j in range(2):
                matrix[y+i][x+j] = count
                count += 1
    else:
        Z(x,y,n-1)
        Z(x+2**(n-1),y,n-1)
        Z(x,y+2**(n-1),n-1)
        Z(x+2**(n-1),y+2**(n-1),n-1)
Z(0,0,n)
print(matrix[r][c])


'''
위의 코드가 내가 처음 짠 코드이다. 처음엔 n이 하나씩 줄어 갈때마다, 4개의 결과가 나온 다는 것을 깨닫고, 
단계당 4번의 재귀함수를 돌며 문제를 풀려고 했었다.
처음 배열을 2^n * 2^n 만큼 빈 배열로 선언하여 이에 재귀문을 돌면서 값을 채워나가는
방식을 택하여 풀었었다. 하지만 이는 메모리를 너무 많이 소모했고 메모리 초과로 오답이 나왔었다.

그래서 다른 방법을 생각하던 도중, 규칙성과 재귀를 이용해 풀어보기로 결심하였다.
아래가 배열 선언 없이 정답이 나온 코드이다.

사분면을 이용해 재귀함수로 계속해서 어느 사분면에 있는지 알아내어 이에 맞는 숫자를 더해가는 방식으로 문제를 풀었다.
'''


n,r,c = map(int, input().split())
count = 0
def Z(r,c,n):
    global count
    n1 = 2**(n-1)
    if(n == 1):
        if(r == 0 and c == 0):
            return
        elif(r == 0 and c == 1):
            count += 1
            return
        elif(r == 1 and c == 0):
            count += 2
            return
        elif(r == 1 and c == 1):
            count += 3
            return
    if(r // n1 == 0 and c // n1 == 0):
        count += 0
    elif(r // n1 == 0 and c // n1 == 1):
        count += (n1**2)
    elif(r // n1 == 1 and c // n1 == 0):
        count += 2*(n1**2)
    else:
        count += 3*(n1**2)
    
    Z(r%n1,c%n1,n-1)

if(n == 1):
    if(r == 0 and c == 0):
        print(0)
    elif(r == 0 and c == 1):
        print(1)
    elif(r == 1 and c == 0):
        print(2)
    else:
        print(3)
else:
    Z(r,c,n)
    print(count)

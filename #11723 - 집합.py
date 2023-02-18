import sys

n = int(input())
FalseList = [False for i in range(20)]


for i in range(n):
    command = sys.stdin.readline().strip()
    if(command[0:2] == 'ad'):
        FalseList[int(command[4:])-1] = True
    elif(command[0] == 'r'):
        FalseList[int(command[7:])-1] = False
    elif(command[0] == 'c'):
        if(FalseList[int(command[6:])-1]):
            print(1)
        else:
            print(0)
    elif(command[0] == 't'):
        if(FalseList[int(command[7:])-1]):
            FalseList[int(command[7:])-1] = False
        else:
            FalseList[int(command[7:])-1] = True
    elif(command[0:2] == 'al'):
        FalseList = [True for i in range(20)]
    else:
        FalseList = [False for i in range(20)]
        
        
'''
이 문제는 구현은 쉽지만 시간초과를 어떻게하면 하지 않을지 고민을 해야 되는 문제이다.
직관적으로 일반적인 리스트로 구현하면 바로 시간 초과가 발생할 것 같아 고민중, True, False로 구현하기로 했다.
왜냐하면 집합이라 중복이 없고, 숫자의 범위가 주어졌기 때문에 각 숫자를 인덱스로 표현하면 쉬웠기 때문이다.

이렇게 무조건 리스트를 먼저 생각하지 말고, 다른 창의적인 방식도 생각하는 회로를 개척해야겠다.
'''

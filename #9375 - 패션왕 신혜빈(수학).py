import sys

t = int(input())

answer = []

for j in range(t):
    n = int(input())
    closet = {}
    counts = 1
    for i in range(n):
        name, close = sys.stdin.readline().split()
        if close not in closet:
            closet[close] = 1
        else:
            closet[close] += 1
    for key in closet.keys():
        counts = counts * (closet[key]+1)
    if (n == 0):
        answer.append(0)
    else:
        answer.append(counts - 1)

for i in answer:
    print(i)

    
'''
위 문제는 코딩을 하는 문제라기보다 수학적으로 어떻게 푸는지가 관건인 문제다.
옷의 종류와 해당 종류의 개수가 주어지고, 이를 조합해서 총 몇개의 경우의 수가 나오는지 계산하는 문제이다.

내가 생각한 알고리즘은 (각각 종류의 개수 + 1)을 모두 곱하고 전체에 -1을 해주는 것이다.
(해당 종류를 입지 않았을때를 위해 + 1을 해주고 아무것도 입지 않은 것은 포함되지 않으므로 계산한 값에 -1을 해준다)

확률과 통계를 생각하며 콤비네이션(C) 순열 등으로 푸려고 했지만 도저히 규칙을 찾을 수 없던 와중에 번뜩 머리속에
위의 알고리즘이 생각이 났다.

가끔씩 이런 수학적인 문제를 푸는것도 신선한 것 같다.
'''

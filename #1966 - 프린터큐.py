n = int(input())
result = []
for i in range(n):
    list_len , num = map(int, input().split())
    numList = list(map(int, input().split()))
    trueList = [True for i in range(list_len)] #포인팅을 위한 TrueList 선언
    trueList[num] = False #찾고자하는 수의 인덱스를 False로 지정
    count = 0

    while(True):
        maxNum = max(numList)
        current = numList.pop(0)
        currentBool = trueList.pop(0)
        if(current < maxNum):
            numList.append(current)
            trueList.append(currentBool)
        elif(current == maxNum):
            count += 1
        
        if(current == maxNum and currentBool is False):
            break
    result.append(count)


for i in result:
    print(i)

'''
배열 하나만 선언하면 포인팅을 할 수 없기 때문에 TrueList를 선언한다
TrueList에서 알고 싶어하는 수를 False로 지정한 다음 False를 포인터로 지정한다.
'''
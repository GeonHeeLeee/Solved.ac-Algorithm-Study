import sys

n = int(input())
result = []

for i in range(n):
    command = sys.stdin.readline().strip()
    number = int(sys.stdin.readline().strip())
    if (number == 0):
        num_list = []
        
    num_list = sys.stdin.readline().strip()[1:-1].split(',')

    flag = False #예외처리
    reverse_count = 0 
    
    for j in range(len(command)):
        if (command[j] == 'R'):
            reverse_count += 1 #reverse시 시간복잡도 문제가 커지므로 count로 해서 마지막에 reverse
        elif (command[j] == 'D'):
            try:
                if (reverse_count % 2 == 0):
                    del num_list[0] #reverse_count에 따라 뒤집었는지 안 뒤집었는지 판단하고 이에 맞는 인덱스의 원소 지우기
                else:
                    del num_list[-1]
            except:
                flag = True
                result.append('error') #빈 배열에서 삭제시 에러 발생 : 예외처리
                break
    if (flag == False):
        if (reverse_count % 2 != 0):
            num_list.reverse() #reverse_count 가 짝수면 뒤집기 후 결과에 추가
            result.append('['+','.join(num_list)+']')
        else:
            result.append('['+','.join(num_list)+']')


for result in result:
    print(result)
    

'''    
이 문제는 쉬운 문제이지만, 문제의 조건과 정답 출력 양식이 이상해 시간을 많이 뺐겼다.

가장 중요한 개념은, 시간복잡도를 줄이기 위해 바로바로 reverse를 하지 않고, reverse 명령마다 count += 1을 해, 마지막에 reverse를 해주는 것이다.
그리고 join, split 함수도 필수로 사용하여야 한다.
'''

import sys

channel = int(input())
m = int(input())

error = list(map(int, sys.stdin.readline().split()))


max_counts = abs(channel - 100)
for num in range(1000001):
    num = str(num)
    
    for i in range(len(num)):
        if int(num[i]) in error:
            break
        
        if(i == len(num) - 1):
            max_counts = min(max_counts, abs(int(num) - channel) + len(num))

print(max_counts)

'''
위 문제는 간단한 브루트포스 알고리즘이다.
모든 경우를 해보면서 조건에 맞는 최적의 답을 찾아내면 되는 문제이다.
이렇게 간단한 문제임에도 시간복잡도가 초과될까 되려 겁을 먹고 효율성을 따지는 코드를 짜려고 애썼다.

밑은 내가 처음 짠 코드이다.
'''

channel = int(input())
channel_list = []
for i in range(1,len(str(channel))+1):
    channel_list.append(channel%(10**i)//(10**(i-1)))
channel_list.reverse()

n = int(input())
if(n != 0):
    error = map(int,sys.stdin.readline().split())
    button = [0,1,2,3,4,5,6,7,8,9]
    for num in error:
        button.remove(num)
else:
    button = [0,1,2,3,4,5,6,7,8,9]
current_channel = 100
pressed_channel = ''
count = 0

if(n == 0):
    print(len(str(channel)))
elif(n == 10):
    print(abs(100 - channel))
else:
    for num in range(len(channel_list)):
        min = 10**len(channel_list)
        if(pressed_channel == ''):
            for i in button:
                if(abs(channel_list[num] - i) < min):
                    number = i
                    min = abs(channel_list[num] - i)
            pressed_channel += str(number)
            count += 1
            continue
        
        for i in range(len(button)):
            current = abs(channel//(10**(len(channel_list) - num-1)) - int(pressed_channel+str(button[i])))
            if(min > current and current != 0):
                min = current
                number = button[i]
        pressed_channel += str(number)
        count += 1

    if(pressed_channel.count('0') == len(pressed_channel)):
        count = 1 + abs(int(pressed_channel) - channel)
    else:
        count += abs(int(pressed_channel) - channel)

    plus_count = abs(channel - 100)

    if(plus_count < count):
        print(plus_count)
    else:
            print(count)
        
        
        
'''
코드도 정말 길고 가독성도 떨어진다. 그래도 문제를 풀어보겠다는 마음가짐으로 일단은 구현부터 해보자 했었지만 수많은 예외처리 상황에 좌절하여 끝내 포기하였다.
이전에도 느꼈었던 것이지만 시간복잡도보다 구현을 우선순위로 생각하는게 좋을 것 같다.
물론 시간복잡도도 중요하지만 처음 간결하게 구현을 해보는것이 중요할 것 같다.
'''

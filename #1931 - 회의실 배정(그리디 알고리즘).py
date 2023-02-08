'''
문제의 발상 :
이 문제는 가장 최적의 해를 구하는 문제로, *그리디 알고리즘(미래를 고려하지 않고 현재에 가장 이득이 되는 것을 고름)을
사용하는 문제이다.

처음 내가 생각한 방식은, 회의의 시간이 가장 짧은 순서대로 정렬해서 매 순간에서 가장 최적을 고르는 방식이였다.
하지만 이는 회의의 시작과 끝남이 뒤죽박죽이였기 때문에 정확하지 않은 알고리즘이였다.

다음은 내가 처음 짠 코드이다.
'''

import sys
n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))
start_time = min(time,key = lambda x : x[0])[0]
end_time = max(time, key = lambda x : x[1])[1]
time_schedule = [False for _ in range(start_time, end_time+1)]

time.sort(key = lambda x : (x[1],x[0]))
current = 0
count = 0
while(current < n):
    current_time = time[current]
    if(time_schedule[current_time[0]] == False and time_schedule[current_time[1]] == False):
        for i in range(current_time[0], current_time[1]):
            time_schedule[i] = True
        count += 1
        current += 1
    else:
        current += 1
print(count)


'''
그래서 두번째로 생각한 것은

1. 끝나는 순서대로 오름차순 정렬
2. 끝나는 순서가 같을 시, 시작 시간을 기준으로 오름차순 정렬
   - 왜냐하면 (3,3) , (1,3) 이렇게 정렬 되어 있을 시, (3,3)이 선택되고 (1,3)은 무시되어 총 가능 횟수가 1번이 됨
   
이를 적용해서 짠 코드가 최종 코드이다.
'''

import sys
n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key = lambda x : (x[1],x[0]))
current = 0
count = 1

print(time)
current = 0
for i in range(1,n):
    end = time[current][1]
    start = time[i][0]
    if(end <= start):
        current = i
        count += 1

print(count)


'''
그리디 알고리즘을 거의 처음 풀어 보는 것 같은데, 이전까지의 방식과 달라서 계속해서 선택 이후의 문제를 고려 하는 것 같다.
그리디 알고리즘을 사용할때에는 현재 상황의 이득만 고려하는 사고방식을 키워야겠다.
'''

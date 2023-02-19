n = int(input())

dp = [1,2,3]

for i in range(3,1000):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n-1]%10007)


'''
해당 문제는 규칙을 발견하면 매우 쉽게 풀리는 문제이다.
n이 주어졌을 때, 2x1 타일과 1x2타일로 2xn타일을 채우는 경우의 수를 구하는 문제이다.

문제를 읽자마자 DP의 느낌이 들어 그림을 그려 점화식을 발견하려고 했다.
그 결과, 현재의 경우의 수가 이전과 그 이전의 경우의 수에 영향을 받는 다는 것을 확인했고 규칙을 발견했다.

n번째 타일의 경우의 수는 n-1번째 타일의 경우의 수 + n-2번째 타일의 경우의 수 였다.

dp[n] = dp[n-1] + dp[n-2] (단, n>2)

따라서 해당 식을 바로 적용하여 문제를 풀었다.

DP문제를 풀다 보니, 어느정도 DP의 유형이 보이기 시작하였고, 이를 구현하는 것도 익숙해지게 되었다.
평소 약했던 부분이라 생각했던 DP가 쉽게 풀리니 뿌듯하고 성취감이 느껴졌다.
'''

n = int(input())
wordList = []
for i in range(n):
    wordList.append(input())

wordList = list(set(wordList))
wordList.sort()
wordList = sorted(wordList,key = lambda x: len(x))
for i in range(len(wordList)):
    print(wordList[i])

'''
lambda는 무명함수로 이름 없는 함수를 작성할 때 사용한다.

예시 )
a = lambda x : x*x
print(a(4)) #16


sorted ([list 혹은 dic], key = lambda x: [key로 지정하고 싶은 요소])

만약 
sorted(dictionary, key = lambda x: x[0]) <<일시 첫번째 요소를 기준으로 배열을 정렬한다.

'''
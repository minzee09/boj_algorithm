#1 단계 - 입출력과 사칙연산

#2557번 - Hello world
print("Hello World!")

#1000번 - a+b
#런타임 에러(ValueError)
#a = int(input())
#b = int(input())

#print(a+b)

#정답
a, b = input().split()
print(int(a) + int(b))

a,b = map(int, input().split())
print(a+b)

#1001번 - a-b
a, b = input().split()
print(int(a) - int(b))

a,b = map(int, input().split())
print(a-b)

#10998번 - axb
a,b = map(int, input().split())
print(a*b)

#1008번 - a/b
#3가지 모두 정답 인정
a,b = map(int, input().split())
print(a/b)

#조건 중 두 정수를 받기에 실수가 올 경우는 X
a,b = map(float, input().split())
print(a/b)

#파이썬은 a/b의 값을 실제 값과 10^-9 이하의 상대오차로 저장하기 때문에 round 함수 필요 X
a,b = map(float, input().split())
print(round(a/b,9))

#10869번 - 사칙연산
a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

#10926번 - ??!
text=input()
print(text + "??!")

#18108번 - 1998년생인 내가 태국에서는 2541년생?!

#int로 변환 안해줘서 오류 발생
#year = input()
#print(year-543)

#정답
year = input()
print(int(year)-543)

#3003번 - 킹, 퀸, 룩, 비숍, 나이트, 폰
#둘다 정답이지만 리스트 사용하는 것이 더 깔끔

k,q,r,b,kn,p =map(int,input().split())
print(1-k, 1-q, 2-r, 2-b, 2-kn, 8-p)

chess = [1,1,2,2,2,8]
a = list(map(int, input().split()))
for i in range(6):
    print(chess[i] - a[i], end=' ')

#10430번 - 나머지
#둘다 정답

a,b,c = map(int, input().split())

#1)
print((a+b)%c)
print(((a%c)+(b%c))%c)

print((a*b)%c)
print(((a%c)*(b%c))%c)

#2)
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n')
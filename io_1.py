#1 단계 - 입출력과 사칙연산

#2557번 - Hello world
print("Hello World!")

#1000번 - A+B
#런타임 에러(ValueError)
#a = int(input())
#b = int(input())

#print(a+b)

#정답
a, b = input().split()
print(int(a) + int(b))

a,b = map(int, input().split())
print(a+b)

#1001번 - A-B
a, b = input().split()
print(int(a) - int(b))

a,b = map(int, input().split())
print(a-b)

#10998번 - AxB
a,b = map(int, input().split())
print(a*b)

#1008번 - A/B
#3가지 모두 정답 인정
a,b = map(int, input().split())
print(a/b)

a,b = map(float, input().split())
print(a/b)

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
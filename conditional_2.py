#2 단계 - 조건문

#1330번 - 두 수 비교하기
a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else :
    print("==")

#9498번 - 시험 성적
score = int(input())

if score >= 90 :
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
### Q1
"""
다음 코드의 결괏값은 무엇일까?

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
"""
# A1 = shirt, wife가 a에 없기 때문에 처음 조건문 실패, python은 있지만 you도 있기 때문에 2번째 조건문도 실패
#      shirt는 a 문자열에 없기 때문에 shirt가 출력된다.



### Q2
"""
while 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자
"""
# A2
"""
a = 0
i = 0
while a < 1001:
    a += 1
    if a % 3 != 0: continue
    else:
      i += a

print(i)
"""

### Q3
"""
while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자
*
**
***
****
*****
"""
# A3
"""
a = 0
while a < 6:
  a += 1
  print("*" * a)
"""


### Q4
"""
for문을 사용해 1부터 100까지의 숫자를 출력해보자
"""
# A4
"""
for i in range(0, 100):
    i += 1
    print(i)
"""

### Q5
"""
A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for 문을 사용하여 A 학급의 평균 점수를 구해보자.
"""
# A5
"""
내 답
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
i = 0
j = 0
for score in scores:
    i += scores[j]
    j += 1
    if j == 10:
      print(i/j)

정답
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score   # A학급의 점수를 모두 더한다.

average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
print(average) # 평균 79.0이 출력된다.
"""



### Q6
"""
리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포(List Somprehension)를 사용하여 표현해보자.
"""

numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 ==1 ]
print(result)

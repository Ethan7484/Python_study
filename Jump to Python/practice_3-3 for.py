### for문의 기본 구조
# for문의 기본 구조는 다음과 같다.

"""
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ....
"""
# 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 "수행할 문장1", "수행할 문장2" 등이 수행된다.


### 예제를 통해 for문 이해하기
# for문은 예쩨를 통해서 살펴보는 것이 가장 알기 쉽다. 다음 예제를 직접 입력해보자.

"""
1. 전형적인 for문
"""
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# ['one', 'two', 'three'] 리스트의 첫 번째 요소인 'one'이 먼저 i 변수에 대입된 후 "print(i)" 문장을 수행한다.
# 다음에 두번째 요소 'two'가 i 변수에 대입된 후 print(i) 문장을 수행ㅎ하고 리스트의 마지막 요소까지 이것을 반복한다.

"""
2. 다양한 for문의 사용
"""
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
# 위 예는 a 리스트의 요소값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입된다.
# 이 예는 02장에서 살펴본 튜플을 사용한 변구값 대입 방법과 매우 비슷한 경우이다.
# >>> (first, last) = (1, 2)

"""
3. for문의 응용
"""
# for문의 쓰임새를 알기 위해 다음을 가정해보자.
# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오."


# 1번 학생은 90점이고 5번 학생은 80점이다.
# 이런 점수를 차례로 검사해서 합격했는지 불합격했는지 통보해 주는 프로그램을 만들어 보자.

# marks1.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark >= 60:
       print("%d번 학생은 합격입니다." % number )
    else:
       print("%d번 학생은 불합격입니다." % number )

"""
for문과 continue
"""
# while문에서 살펴본 continue문을 for문에서도 사용할 수 있다. 즉 for문 안의 문장을 수행하는 도중에 continue문을 만나면 for문의 처음으로 돌아가게 된다.
# 앞에서 for문 응용 예제를 그대로 사용해서 60점 이상인 사람에게 축하 메시지를 보내고 나머지 사람에게는 아무 메시지도 전하지 않는 프로그램을 작성해보자.

# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
      continue
    else:
      print("%d번 학생 축하합니다. 합격입니다. " % number )

"""
for문과 함께 자주 사용하는 range 함수
"""
# for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다. 다음은 range 함수의 간단한 사용법이다.
a = range(10)
# range(10)은 0부터 10미만의 숫자를 포함하는 range 객체를 만들어 준다.

# 시작 숫자와 끝 숫잘를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데, 이때 끝 숫자는 포함되지 않는다.
a = range(1, 11)
print(a)

# range 함수의 예시 살펴보기
# for와 range 함수를 사용하여 1부터 10까지 더하는 것을 구현
add = 0
for i in range(1, 11):
    add += i
print(add)

# marks3.py
marks = [90, 25, 68, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. " % (number+1))


# for와 range를 이용한 구구단
# for와 range 함수를 사용하면 소스 코드 단 4줄만으로 구구단을 출력할 수 있다. 들여쓰기에 주의하며 입력해보자.

for i in range(2, 10):    # 1번 for문
    for j in range(1, 10):    # 2번 for문
        print(i * j, end=" ")
    print('')
# 매개변수 end를 넣어준 이유
# 해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서이다. 그 다음에 이어지는 "print('')"는 2단, 3단을 구분하기 위해
# 두번째 for문이 끝나면 결과값을 다음줄부터 출력하게 해주는 문장이다.


# 리스트 내포 사용하기
# 리스트 안에 for문을 포함하는 리스트 내포(List comprehension)을 사용하면 더 편리하고 직관적인 프로그램을 만들 수 있다.
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)
# 위 예제는 a 리스트의 3을 곱한 결과를 result 리스트에 담는 예이다.
# 이것을 리스트 내포를 사용하면 다음과 같이 간단히 해결할 수 있다.

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 만약 [1, 2, 3, 4] 중에서 짝수에만 3을 곱하여 담고 싶다면 다음과 같이 리스프 내포 안에 "if조건"을 사용할 수 있다.
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)


# 리스트 내포의 일반 문법은 다음과 같다. "if 조건" 부분은 앞의 예제에서 볼 수 있듯이 생략할 수 있다.
"""
[표현식 for 항목 in 반복가능객체 if 조건문]
"""

# 조금 복잡하지만 조건문을 2개 이상 사용하는 것도 가능하다. 구구단을 그렇게 구현해보자.

result = [x * y for x in range(2, 10)
                for y in range(1, 10)]

print(result)
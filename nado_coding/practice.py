### 숫자 자료형
"""
print(5)    # 5가 출력
print(-10)    # 음수도 출력, -10 출력
print(3.14)    # 실수도 출력, 3.14 출력
print(1000)    # 1000 출력
print(5+3)    # 8 출력
print(2*8)    # 16 출력
print(3*(3+1))    # 12 출력
"""

### 문자열 자료형
"""
print('풍선')
print('나비')
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)    # 문자열과 정수를 섞어서 사용할 수 있음
"""


### boolean 자료형
# 참 / 거짓에 대한 자료형
"""
print(5 > 10)    # False
print(5 < 10)    # True
print(True)    # Ture
print(False)    # False
print(not True)    # False
print(not False)    # True
print(not (5 > 10))    # True
"""



### 변수
# 애완동물을 소개해 주세요.
""""
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "이에요")
print(name + "는 " + str(age) + "살 이며, " + hobby + "를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

print("우리집 강아지의 이름은 연탄이에요")
print("연타이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

animal = "고양이"
name = "해피"
age = 2
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "이에요")
hobby = "공놀이"
# print(name + "는 " + str(age) + "살 이며, " + hobby + "를 아주 좋아해요")
print(name,"는 ",str(age),"살 이며, ",hobby ,"를 아주 좋아해요")

print(name + "는 어른일까요? " + str(is_adult))
"""



### 주석


### 퀴즈 #1
'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명
    : station

변수값
    : "사당", "신도림", "인천공항" 순서대로 입력

출력 문장
    : xx행 열차가 들어오고 있습니다.
'''
'''
station1 = "사당"
station2 = "신도림"
station3 = "인천공항"

print(station1 + "행 열차가 들어오고 있습니다.")
print(station2 + "행 열차가 들어오고 있습니다.")
print(station3 + "행 열차가 들어오고 있습니다.")
'''


### 3-1 연산자

print(1+1)    # 2 출력
print(1 + 1)    # 2 출력
print(3 - 1)    # 2 출력
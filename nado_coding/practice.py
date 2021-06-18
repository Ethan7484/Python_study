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

'''
print(1+1)    # 2 출력
print(1 + 1)    # 2 출력
print(3 - 1)    # 2 출력
print(3-2)    # 1
print(5*2)    # 10
print(6/3)    # 2
print(2**3)    # 2의 3제곱, 8 출력
print(5%3)    # 5를 3으로 나눈 나머지, 2출력
print(10%3)    # 10을 3으로 나눈 나머지, 1
print(5//3)    # 5를 3으로 나눈 몫, 1 출력
print(10//3)    # 10을 3으로 나눈 몫, 3 출력

# 비교 연산
print(10 > 3)    # 비교 연산, True 반환
print(4 >= 7)    # False
print(10 < 3)    # False
print(5 <= 5)    # True

print(3 == 3)    # 앞과 뒷의 값이 같은지 확인하는 것, True
print(4 == 2)    # False
print(3+4 == 7)    # True

print(1 != 3)    # !=는 같지 않다는 의미, True
print(not(1 !=3))    # 1은 3과 같지 않다를 다시 not으로 처리 했으니 False

# 2개 이상의 항을 연산
print((3 > 0) and (3 < 5))    # 두 항의 값이 모두 True여야 True 출력
print((3 > 0) & (3 < 5))    # &기호는 and와 같은 의미, True

print((3 > 0) or (3 > 5))    # or 조건은 둘 중에 하나만 True여도, True 출력
print((3 > 0) | (3 > 5))    # | 기호를 or 로 쓸 수 있음, True

print(5 > 4 > 3)    # True
print(5 > 4 > 7)    # 7은 4보다 크기 때문에 False
'''


### 3-2 간단한 수식
'''
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)    # 20
number = 2 + 3 * 4
print(number)
number = number + 2    # number는 14 + 2 = 16
print(number)
number += 2    # number = number +2 와 동일한 구조
print(number)    # 18
number *= 2     # 18 *2 = 36
print(number)    # 36
number /= 2    # 36 / 2 = 18
print(number)    # 18
number -= 2    # 18 - 2 = 16
print(number)    # 16

number %= 2    # 16을 2로 나눴을 때의 나머지, 0
print(number)
'''



### 3-3 숫자 처리 함수
'''
print(abs(-5))    # -5의 대한 절대값을 반환, 5
print(pow(4, 2))    # pow 제곱, 4^2 = 4*4 = 16
print(max(5, 12))    # max는 최대값을 반환, 12
print(min(5, 12))    # min은 최소값을 반환, 5
print(round(3.14))    # round는 반올림하는 함수, 3
print(round(4.99))    # 5
'''



### 3-4 랜덤함수

# from random import *
# print(random())    # 0.0 ~ 1.0 미만의 임의 값 생성
# print(random() * 10)    # 0.0 ~ 10.0 미만의 임의 값 생성
# print(int(random() * 10))    # 0 ~ 10 미만의 임의 값 생성
# print(int(random() * 10) + 1)    # 1 ~ 10 미만의 임의 값 생성

# 로또 값 출력
# print(int(random() * 45) + 1)    # 1 ~ 45 이하의 임의 값 생성
# print(int(random() * 45) + 1)    # 1 ~ 45 이하의 임의 값 생성
# print(int(random() * 45) + 1)    # 1 ~ 45 이하의 임의 값 생성
# print(int(random() * 45) + 1)    # 1 ~ 45 이하의 임의 값 생성
# print(int(random() * 45) + 1)    # 1 ~ 45 이하의 임의 값 생성
# print(int(random() * 45) + 1)    # 1 ~ 45 이하의 임의 값 생성

# 위 값을 좀 더 쉽게
# print(randrange(1, 46))    # 1 ~ 46 미만의 임의 값 생성
# print(randrange(1, 46))    # 1 ~ 46 미만의 임의 값 생성
# print(randrange(1, 46))    # 1 ~ 46 미만의 임의 값 생성
# print(randrange(1, 46))    # 1 ~ 46 미만의 임의 값 생성
# print(randrange(1, 46))    # 1 ~ 46 미만의 임의 값 생성
# print(randrange(1, 46))    # 1 ~ 46 미만의 임의 값 생성

# print(randint(1, 45))    # 1 ~ 45 이하의 임의 값 생성
# print(randint(1, 45))    # 1 ~ 45 이하의 임의 값 생성
# print(randint(1, 45))    # 1 ~ 45 이하의 임의 값 생성
# print(randint(1, 45))    # 1 ~ 45 이하의 임의 값 생성
# print(randint(1, 45))    # 1 ~ 45 이하의 임의 값 생성
# print(randint(1, 45))    # 1 ~ 45 이하의 임의 값 생성




### 3-5 퀴즈 #2
'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데, 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
# from random import *
# study_date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(study_date) + " 일로 선정되었습니다.")
# print("오프라인 스터디 모임 날짜는 매월" , str(study_date),"일로 선정되었습니다.")
# print("오프라인 스터디 모임 날짜는 매월" , study_date,"일로 선정되었습니다.")



### 4-1 문자열

# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = '파이썬은 쉬워요.'
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)



### 4-2 슬라이싱
'''
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])    # 실제 가지고 올 값 다음자리까지 넣어야 함.
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6])    # :을 넣으면 처음부터 인덱스까지 값을 모두 가지고 옴
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:])    # 7:을 넣으면 7부터 끝까지 값을 가지고 옴
print("뒤 7자리(뒤에서부터) : " + jumin[-7:])    # 맨 뒤에서 7번째부터 끝까지 쓸 때는 인덱스를 뒤에서부터 -1로 시작하여 계산
'''



### 4-3 문자열 처리 함수
'''
python = "Python is Amazing"
print(python.lower())    # 문자열을 모두 소문자로
print(python.upper())    # 문자열을 모두 대문자로
print(python[0].isupper())    # python 변수의 0번째 인덱스의 값이 대문자인지 확인하는 구문, True
print(python[0].islower())    # python 변수의 0번째 인덱스의 값이 소문자인지 확인하는 구문, False
print(len(python))    # len을 사용하면 문자열의 길이를 구함
print(python.replace("Python", "Java"))    # 특정 문자열을 찾아서 값을 바꿔주는 함수

index = python.index("n")     # 문자열에서 넣은 값("n")의 위치가 어디인지 인덱스 값을 반환
print(index) 
index = python.index("n", index + 1)    # index + 1을 넣으면 처음 찾은 값 다음부터 다시 찾음
print(index) 

print(python.find("Java"))     # 문자열에 내가 찾는 값이 있는지 확인. -1값을 반환
# print(python.index("Java"))    # index 사용할 때, 찾는 값이 없으면 오류 출력됨.
print(python.count("n"))    # python이라는 변수에 n이 몇번 나오는지 카운트 해주는 것
'''




### 4-4 문자열 포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 20살 입니다.")
# print("나는 %d살 입니다." % 20)    # %d를 넣으면 정수형 값을 넣겠다는 의미
# print("나는 %s를 좋아해요" % "파이썬")     # %s를 넣으면 문자열(스트링)값을 넣겠다는 의미
# print("Apple은 %c로 시작해요." % "A")     # %c는 캐릭터(한 글자)만 넣겠다는 의미

# %s로 바꾸면 문자, 숫자, 캐릭터 구분 없이 사용 가능
# print("나는 %s살 입니다." % 20)
# print("Apple은 %s로 시작해요." % "A")
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))    # %s를 두번 넣으면, 값을 가로 안에 2개 넣으면 됨.


# 방법 2
# print("나는 {}살 입니다." .format(20))     # 이렇게 하면 format 안에 값을 {중가로} 안에 넣을 수 있음
# print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))


# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

# 방법 4 (v 3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")




### 4-5 탈출 문자

# print("백문이 불여일견\n백견이 불여일타")
# print("저는 '나도코딩'입니다.")
# \" \'는 문장 내에서 따옴표
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# print("\\Users\\ethan\\Work\\Python_study\\nado_coding")
# print("/Users/ethan/Work/Python_study/nado_coding")


# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스
# print("Redd\bApple")    # RedApple, d 하나를 지움

# \t : 키보드 탭 키
# print("Red\tApple")




### 4-6 퀴즈#3
'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수와 '!'로 구성
                            (nav)     (5)               (1)        (!)
예) 생성된 비밀번호: nav51!
'''
'''
url = "http://youtube.com"
# rule1 = url[7:]    # 내꺼
rule1 = url.replace("http://", "")    # 정답

# rule2 = rule1[:-4]    # 내꺼
rule2 = rule1[:rule1.index(".")]    # 정답

# rule3 = str(rule2[0:3]) + str(len(rule2)) + str(rule2.count("e")) + "!"    # 내꺼
password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"    # 정답
# print(rule3)
print(password)
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
'''





### 5-1 리스트

# 지하철 칸별로 10명, 20명, 30명
'''
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
'''

'''
# 조세호씨가 몇 번째 칸에 타고 있는가?
subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")    # append => 리스트에 값을 추가 하는 것
print(subway)
# 정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())    # pop 함수로 리스트 마지막 값을 뺄 수 있음
print(subway)

# print(subway.pop()) 
# print(subway)

# print(subway.pop()) 
# print(subway)


# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
'''

# 정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()    # 오름차순으로 정렬
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5, 2, 4, 3, 1]
# mix_list = ["조세호", 20, True]
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)    # extend 함수를 사용하여 두 리스트를 합칠 수 있음
# print(num_list)




### 5-2 사전 (Dictionary)
'''
cabinet = {3:"유재석", 100:"김태호"}     # {key:value} 형태
# print(cabinet[3])    # 딕셔너리에서 키를 넣을 때, [대가로]를 사용
# print(cabinet[100])

# print(cabinet.get(3))

# print(cabinet[5])    # 5라는 키값이 없기 때문에 에러 출력 후 종료
# print(cabinet.get(5))    # get을 사용할 때 값이 없으면 none이라는 값이 출력됨.
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet)    # 3이라는 키값이 cabinet 변수에 존재하므로 True 반환
# print(5 in cabinet)    # 5라는 키값이 cabinet 변수에 없으므로 False 반환

cabinet = {"A-3": "유재석", "B-100": "김태호"}    # 키 값에 문자열도 입력 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새손님
print(cabinet)
cabinet["A-3"] = "김종국"    # 기존값을 업데이트(수정)하는 것
cabinet["C-20"] = "조세호"    # 새로운 값을 추가 하는 것
print(cabinet)



# 간 손님
del cabinet["A-3"]    # del을 사용하면 리스트 값을 삭제할 수 있음
print(cabinet)

# key만 출력
print(cabinet.keys())
# value들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
'''


### 5-3 튜플

'''
menu = ("돈까스", "치즈까스")

print(menu[0])
print(menu[1])

# menu.add("생선까스")    # 튜플은 add를 지원하지 않음

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
'''



### 5-4 세트

'''
# set (집합). 중복 안됨, 순서 없음.
# my_set = {1, 2, 3, 3, 3}    # set에서는 중가로만 쓰면됨
# print(my_set)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 - java와 python을 모두 할 수 있는 개발자.
print(java & python)    # & 교집합
print(java.intersection(python))    # interserction 교집합

# 합칩합 - java도 할 수 있거나 python을 할 수 있는 개발자.
print(java | python)    # | 교집합
print(java.union(python))    # union 교집합

# 차집합 - java는 할 수 있지만 python을 할 수 없는 개발자
print(java - python)    # - 차집합
print(java.difference(python))    # difference 차집합

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)
'''



### 5-5 자료 구조의 변경

'''
# 커피숍
menu = {"커피", "우유", "주소"}
# print(menu)
print(menu, type(menu))    # type을 넣으면 클래스가 출력

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
'''



### 5-6 퀴즈 #4

'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
1st = [1, 2, 3, 4, 5]
print(1st)
shuffle(1st)
print(1st)
print(sample(1st, 1))
'''

'''    실패의 나의 정답
from random import *
lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
print(sample(lst, 1))


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(lst)
chicken = sample(lst, 1)
lst.remove(chicken)
coffee1 = sample(lst, 1)
lst.remove(coffee1)
coffee2 = sample(lst, 1)
lst.remove(coffee2)
coffee3 = sample(lst, 1)
lst.remove(coffee3)
coffee = coffee1 + coffee2 + coffee3
print("""
-- 당첨자 발표 --
치킨 당첨자 : {chicken}
커피 당첨자 : {coffee}
-- 축하합니다 --
""" .format(chicken = chicken, coffee = coffee))
'''

'''
# 교재 정답
from random import *

users = range(1, 21)    # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)     # 4명 중에 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print(" -- 축하 합니다 --")
'''





### 6-1 if
